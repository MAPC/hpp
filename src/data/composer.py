"""
HPP - Composer

Composes Datasets together by running their mungers and
preparing them to be written to files.
"""

from .dataset import Dataset
from .datasets import data_constructors


class Composer(object):

    def __init__(self):
        self.datasets = []

        for constructor in data_constructors:
            self.datasets.append(constructor())    


    def fetch_all(self):
        for dataset in self.datasets:
            dataset.fetch()
