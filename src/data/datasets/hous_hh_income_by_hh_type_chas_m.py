from ..Dataset import Dataset
from pprint import pprint

def hous_hh_income_by_hh_type_chas_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('NEED TO FIND NAME: hous_hh_income_by_hh_type_chas_m')
    dataset.table = 'tabular.hous_hh_income_by_hh_type_chas_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
