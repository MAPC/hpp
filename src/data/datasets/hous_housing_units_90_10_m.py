from ..Dataset import Dataset
from pprint import pprint

def hous_housing_units_90_10_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('hous_housing_units_90_10_m')
    dataset.table = 'tabular.hous_housing_units_90_10_m'
    dataset.munger = munger
    dataset.layout = layout


    return dataset
