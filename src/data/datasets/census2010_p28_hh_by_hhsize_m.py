from ..Dataset import Dataset
from pprint import pprint

def census2010_p28_hh_by_hhsize_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('census2010_p28_hh_by_hhsize_m')
    dataset.table = 'census2010_p28_hh_by_hhsize_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('years', '2010')

    return dataset
