from ..Dataset import Dataset

def hous_shi_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Subsidized Housing Inventory')
    dataset.table = 'hous_shi_m'
    dataset.group = 'affordability'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
