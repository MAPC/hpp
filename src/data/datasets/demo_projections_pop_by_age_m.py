from ..Dataset import Dataset

def demo_projections_pop_by_age_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('demo_projections_pop_by_age_m')
    dataset.table = 'demo_projections_pop_by_age_m'
    dataset.group = 'demographics'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
