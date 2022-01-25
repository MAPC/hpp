from ..Dataset import Dataset

def hous_hh_income_by_hh_type_chas_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Household Income by Household Type')
    dataset.table = 'hous_hh_income_by_hh_type_chas_m'
    dataset.group = 'affordability'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
