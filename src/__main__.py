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
        composer.munis = args.munis
        composer.fetch()
    else:
        gui = GUI(composer)
        gui.launch()


if __name__ == '__main__':
    main()
