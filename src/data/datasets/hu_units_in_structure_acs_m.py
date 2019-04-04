from ..Dataset import Dataset

def hu_units_in_structure_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Housing Units in a Structure')
    dataset.table = 'b25024_hu_units_in_structure_acs_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
