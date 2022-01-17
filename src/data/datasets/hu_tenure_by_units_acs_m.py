from ..Dataset import Dataset

def hu_tenure_by_units_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Household Tenure by Units in Structure')
    dataset.table = 'b25032_hu_tenure_by_units_acs_m'
    dataset.group = 'demographics'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
