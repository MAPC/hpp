"""
HPP - ExcelWriter

ExcelWriter is capable of writing the contents of a DataComposer
to a .xlsx file.
"""

import random
import pandas as pd

import config
from .abbreviate import abbreviate
from .AbstractWriter import AbstractWriter


class ExcelWriter(AbstractWriter):

    file_ext = 'xlsx'

    def __init__(self, *args, **kwargs):
        self.registrations = {}
        self.deferred_registrations = []

        self.colors = [
            '#E53935', # red
            '#AB47BC', # purple
            '#64B5F6', # blue
            '#4DB6AC', # teal
            '#66BB6A', # green
            '#FFD54F', # amber
            '#FF9800', # orange
        ]

        super(ExcelWriter, self).__init__(*args, **kwargs)


    def write(self):
        self._writer = pd.ExcelWriter('%s.%s' % (self.get_output_path(), self.file_ext), engine='xlsxwriter')

        for dataset in self.composer.composed_datasets:
            dataset.render_layout(self)

        colors_by_group = {}
        tables_sorted_by_group = {}
        for group, tables in self.composer.get_datasets_by_group().items():
            for table in tables:
                tables_sorted_by_group[table] = group

            colors_by_group[group] = self.colors.pop(random.randint(0, len(self.colors)))

        for table, group in tables_sorted_by_group.items():
            if table in self.registrations:
                self.process_registration(table, self.registrations[table], colors_by_group[group])

        if len(self.deferred_registrations) > 0:
            for deferred in self.deferred_registrations:
                self.process_registration(deferred['name'], deferred['df'])

        self._writer.save()
        self._writer.close()


    def register(self, name, df):
        if not name in self.registrations:
            self.registrations[name] = df


    def deferred_register(self, name, df):
        self.deferred_registrations.append({ 'name': name, 'df': df })


    def process_registration(self, name, df, color = None):
        if len(name) > 31:
            name = abbreviate(name, 31).title()

        df.to_excel(self._writer, name, index=False)
        sheet = self._writer.sheets[name]

        if color:
            sheet.set_tab_color(color)

        return expand_columns(sheet, df)



def expand_columns(sheet, df):
    for i, col in enumerate(df):
        series = df[col]
        max_len = max([ max([len(x) for x in list(series.astype(str))]), len(col)]) + 1

        if max_len > config.writer.MAX_COL_WIDTH:
            max_len = config.writer.MAX_COL_WIDTH

        res = sheet.set_column(i, i, max_len)
