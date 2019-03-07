from ..dataset import Dataset
from pprint import pprint

def hous_hh_type_size_by_seniors_m():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Household Type/Size by Presence of Seniors')
    dataset.table = 'tabular.hous_hh_type_size_by_seniors_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('years', 2010)

    return dataset
