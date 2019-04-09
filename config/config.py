"""
HPP Configuration - Config declarations

When creating a new config declaration, make sure to expose the new 
declaration by appending it to the import list at the config package root.
"""

from os import environ
from munch import Munch
from dotenv import find_dotenv, load_dotenv
from .defaults import DEFAULTS

load_dotenv(find_dotenv())


def get_value(key):
    return environ.get(key, DEFAULTS.get(key))

def parse_bool(val):
    return bool(str(val).lower() in ('true', 'yes', 't', '1'))

def strip_list(val):
    if val:
        return [x.strip() for x in str(val).split(',')]
    else:
        return val


# Config declarations

args = Munch({
    'FORMAT': get_value('ARGS_FORMAT'),
    'HEADLESS': parse_bool(get_value('ARGS_HEADLESS')),
    'INCLUDE_METADATA': parse_bool(get_value('ARGS_INCLUDE_METADATA')),
    'MUNIS': strip_list(get_value('ARGS_MUNIS')),
    'TABLES': strip_list(get_value('ARGS_TABLES')),
})

prql = Munch({
    'HOST': get_value('PRQL_HOST'),
    'TOKEN': get_value('PRQL_TOKEN'),
})

web = Munch({
    'PORT': int(get_value('WEB_PORT')),
})

writer = Munch({
    'MAX_COL_WIDTH': int(get_value('WRITER_MAX_COL_WIDTH')),
    'MAX_COMPOSITIONS': int(get_values('WRITER_MAX_COMPOSITIONS'))
})
