from ..Dataset import Dataset

def hous_res_sales_by_type_value_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Residential Home Sales by Type and Median Value (Municipal)')
    dataset.table = 'hous_res_sales_by_type_value_m'
    dataset.group = 'demographics'
    dataset.year_column = 'sale_year'
    dataset.munger = munger
    dataset.layout = layout


    return dataset
