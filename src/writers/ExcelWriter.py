"""
HPP - ExcelWriter

ExcelWriter is capable of writing the contents of a DataComposer
to a .xlsx file.
"""

import pandas as pd
from xlsxwriter import Workbook
from .abbreviate import abbreviate
from .AbstractWriter import AbstractWriter


class ExcelWriter(AbstractWriter):

    file_ext = 'xlsx'

    def write(self):
        self._writer = pd.ExcelWriter(self.get_output_path(), engine='xlsxwriter')

        for dataset in self.composer.datasets:
            dataset.render_layout(self)

        self._writer.save()
        self._writer.close()


    def register(self, name, df):
        if len(name) > 31:
            name = abbreviate(name, 31).title()

        df.to_excel(self._writer, name, index=False)

        return self._writer.sheets[name]
