from math import isnan, nan
import pandas as pd
import re


def open_excel(path, encoding='utf8', **kwargs):
    return pd.ExcelFile(path, encoding=encoding, **kwargs)


def open_csv(path, encoding='utf8', **kwargs):
    return pd.read_csv(path, encoding=encoding, **kwargs)


def allsheets(path, encoding='utf8', **parser):   
    file = open_excel(path, encoding=encoding)
    for i, name in enumerate(file.sheet_names):
       yield i, name, file.parse(name, **parser)