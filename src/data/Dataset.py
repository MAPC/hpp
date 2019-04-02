"""
HPP - Dataset

A Dataset describes the way that data should be munged and
interpreted by the rest of the program.
"""

from pprint import pprint
import pandas as pd
from copy import deepcopy

from ..services import prql


class Dataset(object):

    def __init__(self, title = ''):
        self.title = title
        self.data = pd.DataFrame()
        self.metadata = {}
        self.munger = None
        self.layout = None

        self.table = ''
        self.columns = ['*']
        self.length = -1
        self.conditions = {}
        self.sort_by = []
        self.default_condition = 'municipal'
        self.accept_propogations = True

        self.errors = []


    def fetch(self):
        query = self.build_query()

        try:
            data = prql.request(query)
            self.data = pd.DataFrame(data['rows'])
            self.length = len(self.data.index)

            sort_by = self.sort_by if len(self.sort_by) > 0 else list(self.conditions.keys())
            if len(sort_by) > 0 and set(sort_by).issubset(self.data.columns):
                self.data.sort_values(by=sort_by, inplace=True)

        except prql.Error as err:
            self.errors.append(err.response.text)

        return self.length


    def fetch_metadata(self):
        try:
            metadata = prql.request('SELECT alias, name FROM metadata.%s' % self.table)

            for row in metadata['rows']:
                self.metadata[row['name']] = row['alias']

        except prql.Error as err:
            self.errors.append(err.response.text)

        return len(self.metadata.keys())


    def build_query(self):
        query_template = "SELECT %s FROM tabular.%s"

        if len(self.conditions.keys()) > 0:
            condition = ' WHERE '

            conditions = []
            for column, values in self.conditions.items():
                clauses = []

                for value in values:
                    operator = '=' if type(value) == int else 'ILIKE'
                    clauses.append("%s %s '%s'" % (column, operator, value))

                conditions.append('(%s)' % ' OR '.join(clauses))

            query_template = query_template + ' WHERE ' + ' AND '.join(conditions)

        columns = ', '.join(self.columns)
        query = query_template % (columns, self.table)

        return query


    def is_ready_for_use(self):
        if self.length < 0:
            return False, self.errors[-1]
        else:
            return True, None


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


    def render_layout(self, writer):
        if self.layout:
            worksheet = writer.register(self.title, self.data)
            self.layout(worksheet)
        else:
            raise Exception('No layout defined for %s' % (self.table))


    def munge(self):
        if self.munger:
            return self.munger(self.data)
        else:
            raise Exception('No munger defined for %s' % (self.table))
