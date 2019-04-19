from ..Dataset import Dataset

def population_by_age_gender_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Population by Age and Gender')
    dataset.table = 'b01001_population_by_age_gender_acs_m'
    dataset.group = 'demographics'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
