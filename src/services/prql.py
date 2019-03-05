"""
HPP Services - PrQL
"""

import config 
import requests


def prql(query):
    params = {
        'token': config.prql.TOKEN,
        'query': query
    }

    response = requests.get(config.prql.HOST, params=params)
    return response.json()
