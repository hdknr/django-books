from django.db import models
from . import defs, methods

# Create your models here.

class JcbReceipt(defs.JcbReceipt, methods.JcbReceipt):

    class Meta:
        verbose_name = 'JCB明細'
        verbose_name_plural = 'JCB明細'
        unique_together = [
            ['used_on', 'shop', 'used_amount'],
        ]


class JcbShop(defs.JcbShop):

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'