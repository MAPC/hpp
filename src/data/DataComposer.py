"""
HPP - DataComposer

Composes Datasets together by running their mungers and
preparing them to be written to files.
"""

from pprint import pprint

from .Dataset import Dataset
from .datasets import data_constructors
from ..services import prql


class DataComposer(object):

    def __init__(self):
        self.datasets = []
        self.composed_datasets = []

        table_meta = {}
        browser_tables = prql.request('SELECT table_name, source, yearcolumn FROM tabular._data_browser')
        for row in browser_tables['rows']:
            table_meta[row['table_name']] = row

        for constructor in data_constructors:
            self.datasets.append(constructor())    

        for dataset in self.datasets:
            if dataset.table in table_meta:
                dataset.source = table_meta[dataset.table]['source']
                dataset.year_column = table_meta[dataset.table]['yearcolumn']


    def compose(self, munis, tables = None, latest_year = False):
        for muni in munis:
            self.propogate_condition(None, muni)

        fetch_errors = []
        if tables != None:
            for table in tables: 
                table_in_lowercase = table.lower()
                dataset = [dataset for dataset in self.datasets if dataset.title.lower() == table_in_lowercase]

                if len(dataset) > 0:
                    dataset = dataset[0]
                    self.fetch(dataset, latest_year)
                    dataset.munge()
                else:
                    fetch_errors.append("Couldn't find table %s" % table)
        else:
            fetch_errors = self.fetch_all(latest_year)
            self.munge_all()

        if len(fetch_errors) > 0:
            pprint(fetch_errors)


    def fetch(self, dataset, latest_year = False):
        if latest_year:
            dataset.fetch_latest()
        else:
            dataset.fetch()

        dataset.fetch_metadata() 
        self.composed_datasets.append(dataset)

        return dataset.is_ready_for_use()


    def fetch_all(self, latest_year = False):
        errors = []

        for dataset in self.datasets:
            ready, err = self.fetch(dataset, latest_year)
            if not ready:
                errors.append(err)

        return errors


    def munge_all(self):
        for dataset in self.datasets:
            dataset.munge()


    def propogate_condition(self, column, value):
        for dataset in self.datasets:
            if dataset.accept_propogations:
                dataset.add_condition(column, value)


    def get_datasets_by_group(self):
        unsorted_groups = {}
        for dataset in self.datasets:
            group = dataset.group.title()
            if not group in unsorted_groups:
                unsorted_groups[group] = []

            unsorted_groups[group].append({ 
                'title': dataset.title, 
                'source': dataset.source
            })

        table_groups = {}
        for group in sorted(unsorted_groups.keys()):
            table_groups[group] = unsorted_groups[group]

        return table_groups
