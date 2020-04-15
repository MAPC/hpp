"""
HPP Services - PrQL
"""

import config
import requests
from collections import OrderedDict

def request(query):
    params = {
        'token': config.prql.TOKEN,
        'query': query
    }

    response = requests.get(config.prql.HOST, params=params)

    if response.status_code != requests.codes.ok:
        raise Error(response)

    return response.json(object_pairs_hook=OrderedDict)


class Error(Exception):
    def __init__(self, response):
        self.response = response
