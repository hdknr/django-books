from django.db import models
from django.db.models import Sum


class InvoiceQuerySet(models.QuerySet):

    def spendings(self, closed_at__isnull=True, **kwargs):
        kwargs['closed_at__isnull'] = closed_at__isnull 
        return self.filter(
            subclass_type__model='payment', **kwargs
        )

    def incomes(self, closed_at__isnull=True, **kwargs):
        kwargs['closed_at__isnull'] = closed_at__isnull 
        return self.filter(
            subclass_type__model='receipt', **kwargs
        )

    def totals(self):
        return self.aggregate(
            total_amount=Sum('total_amount'),
            tax=Sum('tax'),
            amount=Sum('amount'))