from ..dataset import Dataset
from pprint import pprint

def hh_tenure_by_age_acs_m():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Household Tenure by Age')
    dataset.table = 'tabular.b25007_hh_tenure_by_age_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
