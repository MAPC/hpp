from ..Dataset import Dataset
from pprint import pprint

def hous_projections_hh_by_age_m():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('hous_projections_hh_by_age_m')
    dataset.table = 'tabular.hous_projections_hh_by_age_m'
    dataset.columns = ['muni_id', 'municipal', 'coha', 'age_group', 'hhest_10', 'hh_20_sq', 'hh_30_sq', 'hh_20_sr', 'hh_30_sr']
    dataset.munger = munger
    dataset.layout = layout


    return dataset
