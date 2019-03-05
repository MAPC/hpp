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

prql = Munch({
    'HOST': getValue('PRQL_HOST'),
    'TOKEN': getValue('PRQL_TOKEN'),
})

gui = Munch({
    'TITLE': getValue('GUI_TITLE'),
})
