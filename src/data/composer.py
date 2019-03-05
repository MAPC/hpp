"""
HPP - Composer

Composes Datasets together by running their mungers and
preparing them to be written to files.
"""

class Composer(object):

    def __init__(self):
        self.datasets = []
        self.munis = []


    def fetch(self):
        for dataset in self.datasets:
            dataset.fetch()
