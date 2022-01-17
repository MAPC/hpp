from ..Dataset import Dataset

def costburden_by_age_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Cost Burdened Households by Age')
    dataset.table = 'b25072_b25093_costburden_by_age_acs_m'
    dataset.group = 'affordability'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
