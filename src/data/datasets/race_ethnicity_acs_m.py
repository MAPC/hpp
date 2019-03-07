from ..dataset import Dataset
from pprint import pprint

def race_ethnicity_acs_m():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Race and Ethnicity Estimates')
    dataset.table = 'tabular.b03002_race_ethnicity_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
