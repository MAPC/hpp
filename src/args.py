"""
HPP - Launch arguments
"""

import config
from getopt import getopt


short_args = 'f:hm'
long_args = ['headless', 'format=', 'include-metadata']

def parse_args(args):
    options = getopt(args, short_args, long_args)

    values = {
        'format': config.args.FORMAT,
        'headless': config.args.HEADLESS,
        'tables': config.args.TABLES,
        'munis': config.args.MUNIS if config.args.MUNIS else options[1],
        'include_metadata': config.args.INCLUDE_METADATA,
    }

    for opt, arg in options[0]:
        if opt in ['-h', '--headless']:
            values['headless'] = True

        if opt in ['-m', '--include-metadata']:
            values['include_metadata'] = True

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
