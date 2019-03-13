from ..Dataset import Dataset
from pprint import pprint

def hous_projections_hu_demand_by_age_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('hous_projections_hu_demand_by_age_m')
    dataset.table = 'tabular.hous_projections_hu_demand_by_age_m'
    dataset.munger = munger
    dataset.layout = layout


    return dataset
