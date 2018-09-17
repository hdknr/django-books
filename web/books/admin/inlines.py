from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from django.utils.translation import ugettext_lazy as _
from books import models


class ContactInline(admin.TabularInline):
    model = models.Contact
    exclude = ['created_at']
    readonly_fields = ['updated_at']
    extra = 0


class FisicalYearInline(admin.TabularInline):
    model = models.FisicalYear
    exclude = ['created_at']
    readonly_fields = ['updated_at']
    extra = 0


class BankInline(GenericTabularInline):
    model = models.Bank
    exclude = ['created_at', 'organization']
    readonly_fields = ['updated_at']
    extra = 0
    ct_field = 'owner_content_type'
    ct_fk_field = 'owner_object_id'