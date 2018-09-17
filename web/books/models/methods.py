from django.forms.models import model_to_dict
from django.db.models import Sum


class Attachment(object):

    def has_perm(self, user, perm, **kwargs):
        if user.is_staff:
            return True1G
        return user == self.user


class Invoice(object):

    def dup(self):
        model_class = self.subclass_type.model_class()
        params = vars(self.instance)
        params.pop('id', None)
        params.pop('_state', None)
        params.pop('invoice_ptr_id', None)
        return model_class.objects.create(**params)


class FisicalYear(object):

    def income(self):
        return self.invoice_set.filter(
            subclass_type__model='receipt').aggregate(
                total_amount=Sum('total_amount'),
                tax=Sum('tax'),
                amount=Sum('amount'))

    def spending(self):
        return self.invoice_set.filter(
            subclass_type__model='payment').aggregate(
                total_amount=Sum('total_amount'),
                tax=Sum('tax'),
                amount=Sum('amount'))