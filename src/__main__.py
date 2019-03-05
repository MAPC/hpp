"""
HPP: Housing Production Plan Tool
"""

import sys
from getopt import getopt

from .gui import GUI
from .data import Composer
from .args import parse_args


def main():
    composer = Composer()
    args = parse_args(sys.argv[1:])

    if args['headless']:
        for muni in args['munis']:
            for dataset in composer.datasets:
                dataset.add_condition(dataset.default_condition, muni)

        composer.fetch_all()
    else:
        gui = GUI(composer)
        gui.launch()


if __name__ == '__main__':
    main()
