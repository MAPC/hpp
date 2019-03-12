from ..Dataset import Dataset
from pprint import pprint

def demo_projections_pop_by_age_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('NEED TO FIND NAME: demo_projections_pop_by_age_m')
    dataset.table = 'tabular.demo_projections_pop_by_age_m'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
