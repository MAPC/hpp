"""
HPP - Composer

Composes Datasets together by running their mungers and
preparing them to be written to files.
"""

from .dataset import Dataset


class Composer(object):

    def __init__(self):
        dataset = Dataset('Average Household Size by Tenure')
        dataset.table = 'tabular.b25010_avg_hhsize_by_tenure_acs_m'

        self.datasets = [dataset]
        #self.init_datasets()

    def fetch_all(self):
        for dataset in self.datasets:
            dataset.fetch()
