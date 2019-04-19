from ..Dataset import Dataset

def avg_hhsize_by_tenure_acs_m():

    def munger(data):
        pass

    def layout(worksheet):
        pass

    dataset = Dataset('Average Household Size by Tenure')
    dataset.table = 'b25010_avg_hhsize_by_tenure_acs_m'
    dataset.group = 'housing'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
