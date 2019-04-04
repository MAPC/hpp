"""
HPP - ExcelWriter

ExcelWriter is capable of writing the contents of a DataComposer
to a .xlsx file.
"""

import config
import pandas as pd
from .abbreviate import abbreviate
from .AbstractWriter import AbstractWriter


class ExcelWriter(AbstractWriter):

    file_ext = 'xlsx'

    deferred_registrations = []

    def write(self):
        self._writer = pd.ExcelWriter('%s.%s' % (self.get_output_path(), self.file_ext), engine='xlsxwriter')

        for dataset in self.composer.composed_datasets:
            dataset.render_layout(self)

        if len(self.deferred_registrations) > 0:
            for deferred in self.deferred_registrations:
                self.register(deferred['name'], deferred['df'])

        self._writer.save()
        self._writer.close()


    def deferred_register(self, name, df):
        self.deferred_registrations.append({ 'name': name, 'df': df })


    def register(self, name, df):
        if len(name) > 31:
            name = abbreviate(name, 31).title()

        df.to_excel(self._writer, name, index=False)

        return expand_columns(self._writer.sheets[name], df)


def expand_columns(sheet, df):
    for i, col in enumerate(df):
        series = df[col]
        max_len = max([ max([len(x) for x in list(series.astype(str))]), len(col)]) + 1

        if max_len > config.excel.MAX_COL_WIDTH:
            max_len = config.excel.MAX_COL_WIDTH

        res = sheet.set_column(i, i, max_len)
