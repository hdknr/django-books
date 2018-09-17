from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from . import defs, methods


class Organization(defs.Organization):

    class Meta:
        verbose_name = _('Organization') 
        verbose_name_plural = _('Organizations') 

    def __str__(self):
        return self.name


class Contact(defs.Contact):
    organization = models.ForeignKey(
        Organization, verbose_name=_('Organization'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Contact') 
        verbose_name_plural = _('Contacts') 

    def __str__(self):
        return f"{self.organization} {self.job_title} {self.family_name} {self.first_name}"


class FisicalYear(defs.FisicalYear, methods.FisicalYear):
    organization = models.ForeignKey(
        Organization, verbose_name=_('Organization'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('FiscalYear') 
        verbose_name_plural = _('FiscalYears') 

    def __str__(self):
        return f"{self.organization} {self.name}"



class Bank(defs.Bank):
    organization = models.ForeignKey(
        Organization, verbose_name=_('Organization'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Bank') 
        verbose_name_plural = _('Banks') 

    def __str__(self):
        return f"{self.name} {self.branch} {self.account_type} {self.account} {self.holder}"


class Invoice(defs.Invoice, methods.Invoice):
    fisical_year = models.ForeignKey(
        FisicalYear, verbose_name=_('Fisical Year'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Invoice') 
        verbose_name_plural = _('Invoices') 

    def __str__(self):
        return f"{self.fisical_year} {self.title} {self.total_amount}"


class Receipt(Invoice, defs.Receipt):
    organization = models.ForeignKey(
        Organization, verbose_name=_('Receipt From'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Receipt Invoice') 
        verbose_name_plural = _('Receipt Invoices') 


class Payment(Invoice, defs.Payment):
    organization = models.ForeignKey(
        Organization, verbose_name=_('Payment To'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Payment Invoice') 
        verbose_name_plural = _('Payment Invoices') 



class Attachment(defs.Attachment, methods.Attachment):

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, 
        null=True, blank=True, default=None)

    class Meta:
        verbose_name = _('Attachment') 
        verbose_name_plural = _('Attachments') 
        permissions = (
            ("download_data", _("Download Data")),
        )