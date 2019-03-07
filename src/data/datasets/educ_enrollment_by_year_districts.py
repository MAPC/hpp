from ..dataset import Dataset
from pprint import pprint

def educ_enrollment_by_year_districts():

    def munger(data):
        pprint(data)

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Enrollment by School Year')
    dataset.table = 'tabular.educ_enrollment_by_year_districts'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
