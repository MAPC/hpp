from ..Dataset import Dataset

def hh_income_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Household Income')
    dataset.table = 'b19001_hh_income_acs_m'
    dataset.group = 'affordability'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
