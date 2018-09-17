from django.contrib import admin
from books import models
from app.admin  import register_base
from . import inlines


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Organization._meta.fields]
    exclude = ['created_at']
    readonly_fields = ['updated_at']
    inlines = [
        inlines.FisicalYearInline,
        inlines.BankInline,
        inlines.ContactInline,
    ]

@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Invoice._meta.fields]
    exclude = ['created_at', 'subclass_type']
    readonly_fields = ['updated_at', 'subclass_type']
    list_filter = ['subclass_type']


@admin.register(models.Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in models.Receipt._meta.fields 
        if f.name not in ['created_at', 'updated_at', 'invoice_ptr']]
    exclude = ['created_at', 'subclass_type']
    readonly_fields = ['updated_at']


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in models.Payment._meta.fields
        if f.name not in ['created_at', 'updated_at', 'invoice_ptr']]
    exclude = ['created_at', 'subclass_type']
    readonly_fields = ['updated_at']


@admin.register(models.Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Attachment._meta.fields]

register_base()