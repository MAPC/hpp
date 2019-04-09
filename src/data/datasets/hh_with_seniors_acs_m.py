from ..Dataset import Dataset

def hh_with_seniors_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Households with Seniors')
    dataset.table = 'b11007_hh_with_seniors_acs_m'
    dataset.group = 'housing'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
