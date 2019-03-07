from ..dataset import Dataset
from pprint import pprint

def costburden_acs_m():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Cost Burdened Households')
    dataset.table = 'tabular.b25091_b25070_costburden_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
