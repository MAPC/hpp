from ..Dataset import Dataset
from pprint import pprint

def avg_hhsize_by_tenure_acs_m():

    def munger(data):
        pass

    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Average Household Size by Tenure')
    dataset.table = 'tabular.b25010_avg_hhsize_by_tenure_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
