from ..Dataset import Dataset

def demo_race_ethnicity_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('demo_race_ethnicity_m')
    dataset.table = 'demo_race_ethnicity_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('years', '2010')

    return dataset
