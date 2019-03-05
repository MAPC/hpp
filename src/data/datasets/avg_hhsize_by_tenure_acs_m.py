from ..dataset import Dataset
from pprint import pprint

def avg_hhsize_by_tenure_acs_m():

    def munger(data):
        pprint(data)

    dataset = Dataset('Average Household Size by Tenure')
    dataset.table = 'tabular.b25010_avg_hhsize_by_tenure_acs_m'
    dataset.munger = munger

    return dataset
