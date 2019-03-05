"""
HPP - Dataset

Datasets describe the way that data should be munged and
interpreted by the rest of the program.
"""

import pandas as pd
from ..services import prql


class Dataset(object):

    def __init__(self, title = ''):
        self.title = title
        self.data = []
        self.munger = None

        self.table = ''
        self.columns = ['*']
        self.conditions = {}
        self.default_condition = 'municipal'


    def fetch(self):
        query_template = "SELECT %s FROM %s"

        if len(self.conditions.keys()) > 0:
            condition = ' WHERE '

            clauses = []
            for column, values in self.conditions.items():
                for value in values:
                    clauses.append("%s ILIKE '%s'" % (column, value))

            query_template = query_template + condition + ' OR '.join(clauses)

        columns = ', '.join(self.columns)
        query = query_template % (columns, self.table)
        data = prql(query)

        self.data = pd.DataFrame(data['rows'])

        return len(self.data.index)


    def add_condition(self, column, value):
        if column in self.conditions:
            self.conditions[column].append(value)
        else:
            self.conditions[column] = [value]


    def clear_conditions(self, column = None):
        if column != None:
            self.conditions.pop(column, None)
        else:
            self.conditions = {}


    def set_munger(self, munger):
        self.munger = munger


    def munge(self):
        if self.munger:
            return self.munger(self.data)
        else:
            raise Exception('No munger defined for %s' % (self.table))
