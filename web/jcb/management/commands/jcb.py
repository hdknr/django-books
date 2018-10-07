from django.utils import translation
from django.db.models import Q
import djclick as click
from jcb.models import sheets, JcbReceipt, JcbShop
from math import isnan, nan
import operator
from functools import reduce
from logging import getLogger
log = getLogger()

translation.activate('ja')


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass

def _patch(value):
    if isinstance(value, float) and isnan(value):
        return None
    return value    

def import_receipt_file(path):
    sheet = sheets.open_csv(path, encoding='cp932', skiprows=5)
    mapper = JcbReceipt.get_fields_map()
    for i, row in sheet.iterrows():
        data = row.to_dict()
        data = dict((mapper[k], _patch(v)) for k, v in data.items())
        data['used_on'] = data['used_on'] and data['used_on'].replace('/', '-').replace(' ', '')
        if data['used_on'] and len(data['used_on']) == 7:
            data['used_on'] = data['used_on']  + '-01'
        data['used_amount'] = data['used_amount'] and data['used_amount'].replace(',', '')
        data['paid_amount'] = data['paid_amount'] and data['paid_amount'].replace(',', '')
        JcbReceipt.objects.get_or_create(**data) 


@main.command()
@click.argument('path')
@click.pass_context
def import_receipt(ctx, path):
    '''JCB CSV'''
    import_receipt_file(path)


@main.command()
@click.pass_context
def export_expense(ctx):
    '''Expense Paid JCB'''
    shop = reduce(operator.or_, [Q(shop__contains=i.name) for i in JcbShop.objects.all()])
    mapper = dict((v, k) for k, v in JcbReceipt.get_fields_map().items())

    def _patch(instance, name):
        return '"{}"'.format(
            str(getattr(instance, name, '') or '').replace('\n', ' '))

    click.echo( ','.join(mapper.values()))
    keys = mapper.keys()
    for instance in JcbReceipt.objects.filter(shop).order_by('used_on'):
        click.echo(','.join(_patch(instance, i) for i in keys))