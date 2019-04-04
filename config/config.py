"""
HPP Configuration - Config declarations

When creating a new config declaration, make sure to expose the new 
declaration by appending it to the import list at the package root.
"""

from os import environ
from munch import Munch
from dotenv import find_dotenv, load_dotenv
from .defaults import DEFAULTS

load_dotenv(find_dotenv())

def getValue(key):
    return environ.get(key, DEFAULTS.get(key))


# Config declarations

MUNIS = getValue('ARGS_MUNIS')
if MUNIS:
    MUNIS = [muni.strip() for muni in MUNIS.split(',')]

TABLES = getValue('ARGS_TABLES')
if TABLES:
    TABLES = [table.strip() for table in TABLES.split(',')]

args = Munch({
    'FORMAT': getValue('ARGS_FORMAT'),
    'HEADLESS': getValue('ARGS_HEADLESS'),
    'INCLUDE_METADATA': getValue('ARGS_INCLUDE_METADATA'),
    'MUNIS': MUNIS,
    'TABLES': TABLES,
})

excel = Munch({
    'MAX_COL_WIDTH': int(getValue('EXCEL_MAX_COL_WIDTH')),
})

prql = Munch({
    'HOST': getValue('PRQL_HOST'),
    'TOKEN': getValue('PRQL_TOKEN'),
})

web = Munch({
    'PORT': int(getValue('WEB_PORT')),
})
