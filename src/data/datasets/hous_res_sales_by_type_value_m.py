from ..Dataset import Dataset
from pprint import pprint

def hous_res_sales_by_type_value_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('hous_res_sales_by_type_value_m')
    dataset.table = 'tabular.hous_res_sales_by_type_value_m'
    dataset.munger = munger
    dataset.layout = layout


    return dataset
