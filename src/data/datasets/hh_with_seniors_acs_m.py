from ..Dataset import Dataset
from pprint import pprint

def hh_with_seniors_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Households with Seniors')
    dataset.table = 'b11007_hh_with_seniors_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
