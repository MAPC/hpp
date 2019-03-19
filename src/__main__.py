"""
HPP: Housing Production Plan Tool
"""

import sys

from .web import Server
from .data import DataComposer
from .args import parse_args
from .writers import ExcelWriter, CSVWriter


def main():
    args = parse_args(sys.argv[1:])

    if args['headless']:
        composer = DataComposer()
        composer.compose(args['munis'])
        
        if args['format'] == 'csv':
            writer = CSVWriter(composer)
        else:
            writer = ExcelWriter(composer)

        return writer.write()

    else:
        server = Server()
        return server.serve()


if __name__ == '__main__':
    main()
