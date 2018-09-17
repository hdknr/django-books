from django import forms
from books import models


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = models.Receipt
        exclude = []

    def patch(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patch()


class ReceiptForm(InvoiceForm):

    class Meta:
        model = models.Receipt
        exclude = []

    def patch(self):
        fisical_year = models.FisicalYear.objects.filter(
            self.data.get('fisical_year', 0)).first()
        if fisical_year:
            org = fisical_year.organization
        elif hasattr(self.instance, 'organization'):
            org = self.instance.organization
        if org:
            self.fields['bank'].queryset = \
                self.fields['bank'].queryset.filter(
                    owner_content_type__model='organization',
                    owner_object_id=org.id)


class PaymentForm(InvoiceForm):

    class Meta:
        model = models.Payment
        exclude = []

    def patch(self):
        id = self.instance.organization.id \
            if hasattr(self.instance, 'organization') else None
        id = self.data.get('organization', id)
        if id:
            self.fields['bank'].queryset = \
                self.fields['bank'].queryset.filter(
                    owner_content_type__model='organization',
                    owner_object_id=id)