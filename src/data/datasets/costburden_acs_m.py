from ..Dataset import Dataset

def costburden_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Cost Burdened Households')
    dataset.table = 'b25091_b25070_costburden_acs_m'
    dataset.group = 'affordability'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
