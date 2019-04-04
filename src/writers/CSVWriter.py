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

    file_ext = 'zip'

    def write(self):
        workdir = path.join(gettempdir(), self.file_name)

        try:
            mkdir(workdir, 0o700)
        except OSError:
            print("Could not create directory %s" % workdir)
            return

        for dataset in self.composer.composed_datasets:
            file_path = path.join(workdir, "%s.csv" % dataset.table)
            dataset.data.to_csv(file_path, index=False)

            if self.include_metadata:
                meta_path = path.join(workdir, 'meta_%s.csv' % dataset.table)
                meta_df = dataset.get_formatted_metadata()
                meta_df.to_csv(meta_path, index=False)

        make_archive(self.get_output_path(), self.file_ext, workdir)  

        try:
            rmtree(workdir)
        except OSError:
            print("Could not delete directory %s" % workdir)
            return
