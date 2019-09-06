"""
HPP - Dataset

A Dataset describes the way that data should be munged and
interpreted by the rest of the program.
"""

import pandas as pd
from pprint import pprint

from ..services import prql


class Dataset(object):

    def __init__(self, title = ''):
        self.title = title
        self.data = pd.DataFrame()
        self.metadata = {}
        self.munger = None
        self.layout = None

        self.table = ''
        self.group = ''
        self.columns = ['*']
        self.length = -1
        self.conditions = {}
        self.sort_by = []
        self.source = ''
        self.year_column = ''
        self.default_condition = 'municipal'
        self.accept_propogations = True

        self.errors = []

    def fetch(self):
        query = self.build_query()

        try:
            data = prql.request(query)
            self.data = pd.DataFrame(data['rows'])
            self.length = len(self.data.index)

          
            if 'district' in self.data.columns:
                self.default_condition = 'district'
            
            sort_by_list = self.sort_by if len(self.sort_by) > 0 else [x for x in [self.default_condition, self.year_column] if x != '']

            if 'muni_id' in self.data.columns:
                sort_by_list.insert(0, 'muni_id')
                self.data['muni_id'] = self.data['muni_id'].astype(int)

            sort_by = set(sort_by_list)
            columns = set(self.data.columns)

            if len(sort_by_list) > 0 and sort_by.issubset(columns):
                self.data.sort_values(by=sort_by_list, inplace=True)

            self.data = self.data[sort_by_list + list(columns.difference(sort_by))]

        except prql.Error as err:
            self.errors.append(err.response.text)

        return self.length


    def fetch_latest(self):
        try:
            data = prql.request('SELECT DISTINCT {0} FROM tabular.{1} ORDER BY {0} DESC LIMIT 1'.format(self.year_column, self.table))
            latest_year = data['rows'][0][self.year_column]

            self.add_condition(self.year_column, latest_year)
        except prql.Error as err:
            self.errors.append(err.response.text)
        except Exception as err:
            self.errors.append(err)

        self.fetch()
        self.clear_conditions(self.year_column)


    def fetch_metadata(self):
        if not len(self.metadata.keys()) > 0:
            try:
                metadata = prql.request('SELECT alias, name, details FROM metadata.%s' % self.table)

                for row in metadata['rows']:
                    self.metadata[row['name']] = row

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


    def get_formatted_metadata(self):
        meta_df = pd.DataFrame(self.metadata.values())
        meta_df = meta_df[['name', 'alias', 'details']]
        meta_df.rename(columns={'name': 'Name', 'alias': 'Alias', 'details': 'Details'}, inplace=True)

        return meta_df


    def render_layout(self, writer):
        if self.layout:
            if len(self.metadata.keys()) > 0:
                metadata_cols = {}
                for name, meta in self.metadata.items():
                    metadata_cols[name] = meta['alias']

                self.data.rename(columns=metadata_cols, inplace=True)

                if writer.include_metadata:
                    meta_df = self.get_formatted_metadata()
                    writer.deferred_register('META %s' % self.title, meta_df)

            worksheet = writer.register(self.title, self.data, writer.colors[self.group])
            self.layout(worksheet)

        else:
            raise Exception('No layout defined for %s' % (self.table))


    def munge(self):
        if self.munger:
            return self.munger(self.data)
        else:
            raise Exception('No munger defined for %s' % (self.table))
