"""
HPP Configuration - Config declarations

When creating a new config declaration, make sure to expose the new 
declaration by appending it to the import list at the config package root.
"""

from os import environ
from munch import Munch
from dotenv import find_dotenv, load_dotenv

from .defaults import DEFAULTS
from src.util import parse_bool, strip_list


load_dotenv(find_dotenv())

def get_value(key):
    return environ.get(key, DEFAULTS.get(key))


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
    'MAX_COMPOSITIONS': int(get_value('WRITER_MAX_COMPOSITIONS'))
})
