from ..Dataset import Dataset

def census2010_p28_hh_by_hhsize_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('census2010_p28_hh_by_hhsize_m')
    dataset.table = 'census2010_p28_hh_by_hhsize_m'
    dataset.group = 'housing'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
