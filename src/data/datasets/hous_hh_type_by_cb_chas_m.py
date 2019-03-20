from ..Dataset import Dataset
from pprint import pprint

def hous_hh_type_by_cb_chas_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Household Type by Cost Burden Status')
    dataset.table = 'tabular.hous_hh_type_by_cb_chas_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2011-15')

    return dataset
