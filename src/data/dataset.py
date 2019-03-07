"""
HPP - Dataset

Datasets describe the way that data should be munged and
interpreted by the rest of the program.
"""

import pandas as pd
from copy import deepcopy
from requests import HTTPError
from ..services import prql
from pprint import pprint


class Dataset(object):

    def __init__(self, title = ''):
        self.title = title
        self.data = []
        self.munger = None

        self.table = ''
        self.columns = ['*']
        self.fresh = False
        self.conditions = {}
        self.previous_conditions = None
        self.default_condition = 'municipal'
        self.accept_propogations = True

        self.errors = []


    def fetch(self):
        if not self.is_fresh():
            self.previous_conditions = deepcopy(self.conditions)

            query_template = "SELECT %s FROM %s"

            if len(self.conditions.keys()) > 0:
                condition = ' WHERE '

                clauses = []
                for column, values in self.conditions.items():
                    for value in values:
                        operator = '=' if type(value) == int else 'ILIKE'
                        clauses.append("%s %s '%s'" % (column, operator, value))

                query_template = query_template + condition + (' OR '.join(clauses))

            columns = ', '.join(self.columns)
            query = query_template % (columns, self.table)

            try:
                data = prql.request(query)
                self.data = pd.DataFrame(data['rows'])
                self.length = len(self.data.index)
            except prql.Error as err:
                self.errors.append(err.response.text)
                self.length = -1

        return self.length


    def is_fresh(self):
        return self.conditions == self.previous_conditions


    def is_ready_for_use(self):
        if self.is_fresh():
            if self.length < 0:
                return False, self.errors[-1]
            else:
                return True, None
        else:
            return False, None


    def add_condition(self, column, value):
        if column == None:
            column = self.default_condition

        if column in self.conditions:
            self.conditions[column].append(value)
        else:
            self.conditions[column] = [value]


    def clear_conditions(self, column = None):
        if column != None:
            self.conditions.pop(column, None)
        else:
            self.conditions = {}


    def munge(self):
        if self.munger:
            return self.munger(self.data)
        else:
            raise Exception('No munger defined for %s' % (self.table))
