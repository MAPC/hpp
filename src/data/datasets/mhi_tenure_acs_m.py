from ..Dataset import Dataset

def mhi_tenure_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Median Household Income by Tenure')
    dataset.table = 'b25119_mhi_tenure_acs_m'
    dataset.group = 'affordability'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
