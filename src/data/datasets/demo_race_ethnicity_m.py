from ..Dataset import Dataset

def demo_race_ethnicity_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Population by Race and Ethnicity (Municipal)')
    dataset.table = 'demo_race_ethnicity_m'
    dataset.group = 'demographics'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
