from ..Dataset import Dataset
from pprint import pprint

def rent_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Gross Rent')
    dataset.table = 'tabular.b25063_b25064_b25065_rent_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
