from ..Dataset import Dataset

def hu_occupancy_by_tenure_race_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Household Tenure by Race')
    dataset.table = 'b25002_b25003_hu_occupancy_by_tenure_race_acs_m'
    dataset.group = 'demographics'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
