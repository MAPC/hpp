"""
HPP - Launch arguments
"""

from getopt import getopt


short_args = 'h'
long_args = ['headless']

def parse_args(args):
    options = getopt(args, short_args, long_args)

    values = {
        'headless': False,
        'munis': options[1]
    }

    for opt, arg in options[0]:
        if opt in ['-h', '--headless']:
            values['headless'] = True

    return values
