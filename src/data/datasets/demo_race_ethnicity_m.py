from ..Dataset import Dataset
from pprint import pprint

def demo_race_ethnicity_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('NEED TO FIND NAME: demo_race_ethnicity_m')
    dataset.table = 'tabular.demo_race_ethnicity_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('years', '2010')

    return dataset
