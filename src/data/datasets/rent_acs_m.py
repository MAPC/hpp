from ..Dataset import Dataset

def rent_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Gross Rent')
    dataset.table = 'b25063_b25064_b25065_rent_acs_m'
    dataset.group = 'affordability'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
