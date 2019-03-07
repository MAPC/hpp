from ..dataset import Dataset
from pprint import pprint

def hu_units_in_structure_acs_m():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Housing Units in a Structure')
    dataset.table = 'tabular.b25024_hu_units_in_structure_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
