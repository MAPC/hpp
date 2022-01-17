from ..Dataset import Dataset

def costburden_by_income_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Cost Burdened Households by Income')
    dataset.table = 'b25106_costburden_by_income_acs_m'
    dataset.group = 'affordability'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
