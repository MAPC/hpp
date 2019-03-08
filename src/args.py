"""
HPP - Launch arguments
"""

import config
from getopt import getopt



short_args = 'f:h'
long_args = ['headless', 'format=']

def parse_args(args):
    options = getopt(args, short_args, long_args)

    values = {
        'format': config.args.FORMAT,
        'headless': config.args.HEADLESS,
        'munis': options[1]
    }

    for opt, arg in options[0]:
        if opt in ['-h', '--headless']:
            values['headless'] = True

        if opt in ['-f', '--format']:
            formats = {
                'c': 'csv',
                'csv': 'csv',
                'e': 'excel',
                'excel': 'excel',
            }

            if arg in formats.keys():
                values['format'] = formats[arg]
            else:
                print("WARNING: '%s' is not a valid format. Using '%s'." % (arg, values['format']))
            

    return values
