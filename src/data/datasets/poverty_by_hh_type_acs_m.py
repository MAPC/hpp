from ..Dataset import Dataset
from pprint import pprint

def poverty_by_hh_type_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Households in Poverty by Household Type')
    dataset.table = 'b17017_poverty_by_hh_type_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
