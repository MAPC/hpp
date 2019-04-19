from ..Dataset import Dataset

def hh_tenure_by_age_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Household Tenure by Age')
    dataset.table = 'b25007_hh_tenure_by_age_acs_m'
    dataset.group = 'housing'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
