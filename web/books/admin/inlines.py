from django.contrib import admin
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


class BankInline(admin.TabularInline):
    model = models.Bank
    exclude = ['created_at']
    readonly_fields = ['updated_at']
    extra = 0