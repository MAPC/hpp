from ..Dataset import Dataset

def hous_hh_type_size_by_seniors_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Household Type and Size by Presence of Seniors')
    dataset.table = 'hous_hh_type_size_by_seniors_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('years', 2010)

    return dataset
