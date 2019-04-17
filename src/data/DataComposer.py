"""
HPP - DataComposer

Composes Datasets together by running their mungers and
preparing them to be written to files.
"""

from .Dataset import Dataset
from .datasets import data_constructors
from pprint import pprint


class DataComposer(object):

    def __init__(self):
        self.datasets = []
        self.composed_datasets = []

        for constructor in data_constructors:
            self.datasets.append(constructor())    

        self.fetch_all_metadata()


    def compose(self, munis, tables = None):
        for muni in munis:
            self.propogate_condition(None, muni)

        fetch_errors = []
        if tables != None:
            for table in tables: 
                table_in_lowercase = table.lower()
                dataset = [dataset for dataset in self.datasets if dataset.title.lower() == table_in_lowercase]

                if len(dataset) > 0:
                    dataset = dataset[0]
                    self.fetch(dataset)
                    dataset.munge()
                else:
                    fetch_errors.append("Couldn't find table %s" % table)
        else:
            fetch_errors = self.fetch_all()
            self.munge_all()

        if len(fetch_errors) > 0:
            pprint(fetch_errors)


    def fetch(self, dataset):
        dataset.fetch()
        self.composed_datasets.append(dataset)

        return dataset.is_ready_for_use()


    def fetch_all(self):
        errors = []

        for dataset in self.datasets:
            ready, err = self.fetch(dataset)
            if not ready:
                errors.append(err)

        return errors


    def fetch_all_metadata(self):
        for dataset in self.datasets:
            dataset.fetch_metadata()


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

            source = None
            if 'creator' in dataset.metadata:
                source = dataset.metadata['creator']['details']

            unsorted_groups[group].append({ 
                'title': dataset.title, 
                'source': source
            })

        table_groups = {}
        for group in sorted(unsorted_groups.keys()):
            table_groups[group] = unsorted_groups[group]

        return table_groups
