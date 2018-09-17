from django.db import models
from django.utils.translation import ugettext_lazy as _
from mymedia.files import ModelFieldPath
from app.models import defs as app_defs


class Organization(app_defs.Timestamp):
    name = models.CharField(
        _('Origanization Name'), max_length=50,)

    division = models.CharField(
        _('Origanization Divition'), max_length=100,
        null=True, default=None, blank=True,)

    postal_code = models.CharField(
        _('Postal Code'), max_length=10,
        null=True, default=None, blank=True,)

    prefecture = models.CharField(
        _('Prefecture'), max_length=15,
        null=True, default=None, blank=True,)

    city = models.CharField(
        _('City'), max_length=30,
        null=True, default=None, blank=True,)

    town = models.CharField(
        _('Town'), max_length=100,
        null=True, default=None, blank=True,)

    building = models.CharField(
        _('Building'), max_length=100,
        null=True, default=None, blank=True,)

    phone = models.CharField(
        _('Phone'), max_length=15,
        null=True, default=None, blank=True,)

    fax = models.CharField(
        _('Fax'), max_length=15,
        null=True, default=None, blank=True,)

    class Meta:
        abstract = True

class Contact(app_defs.Timestamp):
    family_name = models.CharField(
        _('Faminly Name'), max_length=50,)
    first_name = models.CharField(
        _('First Name'), max_length=50,)
    job_title = models.CharField(
        _('Job Title'), max_length=50,
        null=True, blank=True, default=None)

    email = models.EmailField(
        _('Email'), null=True, blank=True, default=None)

    class Meta:
        abstract = True

class FisicalYear(app_defs.Timestamp):
    name = models.CharField(
        _('Fisical Year Name'), max_length=50,)

    class Meta:
        abstract = True


BANK_ACCOUNT_TYPES = ['普通', '当座']
BANK_ACCOUNT_TYPE_CHOICES = tuple((i, i) for i in BANK_ACCOUNT_TYPES)


class Bank(app_defs.Timestamp):
    name = models.CharField(
        _('Bank Name'), max_length=50,)
    branch = models.CharField(
        _('Bank Branch Name'), max_length=50,)
    holder = models.CharField(
        _('Account Holder Name'), max_length=50,)
    
    account_type = models.CharField(
        _('Account Type'), max_length=10,
        choices=BANK_ACCOUNT_TYPE_CHOICES, )
    account = models.CharField(
        _('Account Number'), max_length=20,)

    class Meta:
        abstract = True


class Invoice(app_defs.SuperModel, app_defs.Timestamp):
    '''請求書'''
    title = models.CharField(
        _('Invoice Title'), max_length=100,)
    sub_title = models.CharField(
        _('Invoice Sub Title'), max_length=100, 
        null=True, blank=True, default=None)
    number = models.CharField(
        _('Invoice Number'), max_length=50,)
    total_amount = models.DecimalField(
        _('Total Amount'), max_digits=7, decimal_places=0)
    amount = models.DecimalField(
        _('Amount'), max_digits=7, decimal_places=0)
    tax = models.DecimalField(
        _('Tax'), max_digits=7, decimal_places=0)
    rmarks = models.TextField(
        _('Invoice Remarks'), null=True, blank=True, default=None)
    due_at = models.DateTimeField(
        _('Due At'), null=True, blank=True, default=None)
    closed_at = models.DateTimeField(
        _('Closed At'), null=True, blank=True, default=None)

    class Meta:
        abstract = True


class Receipt(models.Model):
    '''受注(入金)'''

    class Meta:
        abstract = True


class Payment(models.Model):
    '''発注(出金)'''

    class Meta:
        abstract = True


class Attachment(app_defs.Timestamp):
    name = models.CharField(max_length=200, null=True, blank=True, default=None)
    data = models.FileField(upload_to=ModelFieldPath('data'))
    description = models.TextField(null=True, blank=True, default=None)

    class Meta:
        abstract = True