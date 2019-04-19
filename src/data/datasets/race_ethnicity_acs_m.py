from ..Dataset import Dataset

def race_ethnicity_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Race and Ethnicity Estimates')
    dataset.table = 'b03002_race_ethnicity_acs_m'
    dataset.group = 'demographics'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
