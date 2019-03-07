from ..dataset import Dataset
from pprint import pprint

def hous_shi_m():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Subsidized Housing Inventory')
    dataset.table = 'tabular.hous_shi_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('shi_date', '2017-09')

    return dataset
