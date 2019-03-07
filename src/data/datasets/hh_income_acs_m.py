from ..dataset import Dataset
from pprint import pprint

def hh_income_acs_m():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Household Income')
    dataset.table = 'tabular.b19001_hh_income_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
