from ..Dataset import Dataset

def hous_shi_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Subsidized Housing Inventory')
    dataset.table = 'hous_shi_m'
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('shi_date', '2017-09')

    return dataset
