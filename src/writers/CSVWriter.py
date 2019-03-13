"""
HPP - CSVWriter

CSVWriter is capable of writing the contents of a DataComposer
to a .csv file.
"""

from os import path, mkdir
from tempfile import gettempdir
from shutil import make_archive, rmtree

from .AbstractWriter import AbstractWriter


class CSVWriter(AbstractWriter):

    def write(self):
        workdir = path.join(gettempdir(), self.file_name)

        try:
            mkdir(workdir, 0o700)
        except OSError:
            print("Could not create directory %s" % workdir)
            return

        for dataset in self.composer.datasets:
            file_path = path.join(workdir, "%s.csv" % dataset.table)
            dataset.data.to_csv(file_path, index=False)

        make_archive(self.file_name, 'zip', workdir)  

        try:
            rmtree(workdir)
        except OSError:
            print("Could not delete directory %s" % workdir)
            return
