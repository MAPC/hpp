from ..dataset import Dataset
from pprint import pprint

def costburden_acs_m():

    def munger(data):
        pprint(data)

    dataset = Dataset('Cost Burdened Households')
    dataset.table = 'tabular.b25091_b25070_costburden_acs_m'
    dataset.munger = munger

    return dataset
