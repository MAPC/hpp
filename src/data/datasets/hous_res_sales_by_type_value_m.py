from ..dataset import Dataset
from pprint import pprint

def hous_res_sales_by_type_value_m():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('NEED TO FIND NAME: hous_res_sales_by_type_value_m')
    dataset.table = 'tabular.hous_res_sales_by_type_value_m'
    dataset.munger = munger
    dataset.layout = layout


    return dataset
