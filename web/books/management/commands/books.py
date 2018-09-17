from django.utils import translation ,timezone
from django.conf import settings
from datetime import datetime, time, timedelta
import djclick as click
from logging import getLogger
from collections import OrderedDict
import requests
import yaml
import os
import uuid
import itertools
from books import models
log = getLogger()

translation.activate('ja')

DOC_PATH = os.path.join(os.path.dirname(settings.BASE_DIR), 'docs')


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.argument('invoice_id')
@click.pass_context
def dup_invoice(ctx, invoice_id):
    '''複製する'''
    invoice = models.Invoice.objects.filter(id=invoice_id).first()
    if invoice:
        instance = invoice.dup()


@main.command()
@click.argument('fisical_year_id')
@click.pass_context
def fisical_year(ctx, fisical_year_id):
    '''数字'''
    year = models.FisicalYear.objects.filter(id=fisical_year_id).first()
    if year:
        click.echo(year.income())
        click.echo(year.spending())