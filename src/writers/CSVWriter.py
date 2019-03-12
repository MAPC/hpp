"""
HPP - CSVWriter

CSVWriter is capable of writing the contents of a DataComposer
to a .csv file.
"""

from .AbstractWriter import AbstractWriter


class CSVWriter(AbstractWriter):

    def write(self):
        print('Writing CSV')
