
from django.db import models
from django.utils.translation import ugettext_lazy as _


class JcbReceipt(models.Model):
    customer = models.CharField('ご利用者', max_length=100)
    category = models.CharField('カテゴリ', max_length=100)
    used_on = models.DateField(
        'ご利用日', null=True, blank=True, default=None)
    shop = models.CharField('ご利用先など', max_length=100)
    used_amount = models.DecimalField(
        'ご利用金額(￥)', max_digits=7, decimal_places=0, 
        null=True, blank=True, default=None)
    payment = models.CharField(
        '支払区分', max_length=50, 
        null=True, blank=True, default=None)
    paynumber = models.CharField('今回回数', max_length=50, null=True, blank=True, default=None, )
    correction = models.CharField('訂正サイン', max_length=50, null=True, blank=True, default=None, )
    paid_amount = models.DecimalField(
        'お支払い金額(￥)', max_digits=7, decimal_places=0,
        null=True, blank=True, default=None)
    national = models.CharField(
        '国内／海外', max_length=50, null=True, blank=True, default=None, )
    summary = models.CharField(
        '摘要', max_length=100, null=True, blank=True, default=None, )
    remarks = models.CharField(
        '備考', max_length=100, null=True, blank=True, default=None, )

    class Meta:
        abstract = True


class JcbShop(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(
        null=True, blank=True, default=None, )
    class Meta:
        abstract = True
