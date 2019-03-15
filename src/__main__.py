"""
HPP: Housing Production Plan Tool
"""

import sys

from src.gui import GUI
from src.data import DataComposer
from src.args import parse_args
from src.writers import ExcelWriter, CSVWriter


def main():
    composer = DataComposer()
    args = parse_args(sys.argv[1:])

    if args['headless']:
        for muni in args['munis']:
            composer.propogate_condition(None, muni)

        composer.compose()
        
        if args['format'] == 'csv':
            writer = CSVWriter(composer)
        else:
            writer = ExcelWriter(composer)

        return writer.write()

    else:
        gui = GUI(composer)
        return gui.launch()


if __name__ == '__main__':
    main()
