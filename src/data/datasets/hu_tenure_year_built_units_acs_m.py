from ..Dataset import Dataset

def hu_tenure_year_built_units_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Housing Tenure by Year Built')
    dataset.table = 'b25127_hu_tenure_year_built_units_acs_m'
    dataset.group = 'housing'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
