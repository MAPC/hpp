"""
HPP - Dataset

Datasets describe the way that data should be munged and
interpreted by the rest of the program.
"""

import pandas as pd


class Dataset(object):

    def __init__(self):
        self.data = []
        self.criteria = []


    def fetch(self):
        for criterion in self.criteria:
            self.fetch_cunk(self, criteria)


    def fetch_chunk(self, criteria):
        print("")


    def _consolidate(self):
        print("")
