"""
HPP - ExcelWriter

ExcelWriter is capable of writing the contents of a DataComposer
to a .xlsx file.
"""

import random
import pandas as pd
from pprint import pprint

import config
from ..util import abbreviate
from .AbstractWriter import AbstractWriter


class ExcelWriter(AbstractWriter):

    TAB_LENGTH = 31 # Excel can't take anymore character than 31

    file_ext = 'xlsx'

    def __init__(self, *args, **kwargs):
        self.deferred_registrations = []

        super(ExcelWriter, self).__init__(*args, **kwargs)

        color_pool = [
            '#E53935', # red
            '#AB47BC', # purple
            '#64B5F6', # blue
            '#4DB6AC', # teal
            '#66BB6A', # green
            '#FFD54F', # amber
            '#FF9800', # orange
        ]

        self.colors = {}
        for group, tables in self.composer.get_datasets_by_group().items():
            self.colors[group.lower()] = color_pool.pop(random.randint(0, len(color_pool) - 1))


    def write(self):
        self._writer = pd.ExcelWriter('%s.%s' % (self.get_output_path(), self.file_ext), engine='xlsxwriter')

        grouped_datasets = self.composer.get_datasets_by_group()
        self.register_table_of_contents(grouped_datasets)

        for datasets in grouped_datasets.values():
            for dataset in datasets:
                if dataset in self.composer.composed_datasets:
                    dataset.render_layout(self)

        if len(self.deferred_registrations) > 0:
            for deferred in self.deferred_registrations:
                self.register(deferred['name'], deferred['df'])

        self._writer.save()
        self._writer.close()


    def register(self, name, df, color = None):
        if len(name) > self.TAB_LENGTH:
            name = abbreviate(name, self.TAB_LENGTH).title()

        df.to_excel(self._writer, name, index=False)
        sheet = self._writer.sheets[name]

        if color:
            sheet.set_tab_color(color)

        return expand_columns(sheet, df)


    def deferred_register(self, name, df):
        self.deferred_registrations.append({ 'name': name, 'df': df })


    def register_table_of_contents(self, groups):
        def nextrow():
            nextrow.cursor = nextrow.cursor + 1
            return 'B%d' % nextrow.cursor
        nextrow.cursor = 1

        bold_fmt = self._writer.book.add_format({'bold': True})
        url_fmt = self._writer.book.get_default_url_format()

        toc = self._writer.book.add_worksheet('Table of Contents')
        toc.set_tab_color('#FFFFFF')

        toc.write(nextrow(), 'Table of Contents', bold_fmt)
        
        for group, datasets in groups.items():
            to_render = []
            for dataset in datasets:
                if dataset in self.composer.composed_datasets:
                    to_render.append(dataset)

            if len(to_render) > 0:
                toc.write(nextrow(), group.title(), bold_fmt)

                for dataset in to_render:
                    tab = dataset.title.title()
                    toc.write_url(nextrow(), "internal:'%s'!A1" % abbreviate(tab, self.TAB_LENGTH), url_fmt, tab)

                nextrow() # skip a row



def expand_columns(sheet, df):
    for i, col in enumerate(df):
        series = df[col]
        max_len = max([ max([len(x) for x in list(series.astype(str))]), len(col)]) + 1

        if max_len > config.writer.MAX_COL_WIDTH:
            max_len = config.writer.MAX_COL_WIDTH

        res = sheet.set_column(i, i, max_len)

    return sheet
