"""
HPP: Housing Production Plan Tool
"""

import sys
from pprint import pprint

from .gui import GUI
from .data import DataComposer
from .args import parse_args


def main():
    composer = DataComposer()
    args = parse_args(sys.argv[1:])

    if args['headless']:
        for muni in args['munis']:
            composer.propogate_condition(None, muni)

        composer.fetch_all()
        composer.munge_all()

    else:
        gui = GUI(composer)
        gui.launch()


if __name__ == '__main__':
    main()
