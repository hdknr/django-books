from django.contrib import admin
from django.contrib import admin
from jcb import models


@admin.register(models.JcbReceipt)
class JcbReceiptAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.JcbReceipt._meta.fields]
    date_hierarchy = 'used_on'
    search_fields = ['shop']


@admin.register(models.JcbShop)
class JcbShopAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.JcbShop._meta.fields]