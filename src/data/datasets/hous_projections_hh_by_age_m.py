from ..Dataset import Dataset

def hous_projections_hh_by_age_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('hous_projections_hh_by_age_m')
    dataset.table = 'hous_projections_hh_by_age_m'
    dataset.group = 'demographics'
    dataset.columns = ['muni_id', 'municipal', 'coha', 'age_group', 'hhest_10', 'hh_20_sq', 'hh_30_sq', 'hh_20_sr', 'hh_30_sr']
    dataset.munger = munger
    dataset.layout = layout


    return dataset
