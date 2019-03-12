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

        for constructor in data_constructors:
            self.datasets.append(constructor())    


    def compose(self):
        fetch_errors = self.fetch_all() 

        if len(fetch_errors) > 0:
            pprint(fetch_errors)

        self.munge_all()


    def fetch_all(self):
        errors = []

        for dataset in self.datasets:
            rows = dataset.fetch()

            ready, err = dataset.is_ready_for_use()
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

