"""
HPP - Dataset

Datasets describe the way that data should be munged and
interpreted by the rest of the program.
"""

import pandas as pd


class Dataset(object):

    def __init__(self):
        self.data = []
