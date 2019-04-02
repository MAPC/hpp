from ..Dataset import Dataset
from pprint import pprint

def hous_hh_income_by_hh_type_chas_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('hous_hh_income_by_hh_type_chas_m')
    dataset.table = 'hous_hh_income_by_hh_type_chas_m'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
