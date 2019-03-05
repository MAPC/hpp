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
        print("Hello world")
    else:
        gui = GUI(composer)
        gui.start()



if __name__ == '__main__':
    main()
