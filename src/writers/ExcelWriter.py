"""
HPP - ExcelWriter

ExcelWriter is capable of writing the contents of a DataComposer
to a .xlsx file.
"""

from .AbstractWriter import AbstractWriter


def ExcelWriter(AbstractWriter):

    def write(self):
        print('Writing Excel')
