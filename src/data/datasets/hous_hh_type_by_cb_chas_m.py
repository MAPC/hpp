from ..Dataset import Dataset

def hous_hh_type_by_cb_chas_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Household Type by Cost Burden Status')
    dataset.table = 'hous_hh_type_by_cb_chas_m'
    dataset.group = 'affordability'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2011-15')

    return dataset
