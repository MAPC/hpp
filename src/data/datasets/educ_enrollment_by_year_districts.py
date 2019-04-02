from ..Dataset import Dataset
from pprint import pprint

def educ_enrollment_by_year_districts():

    def munger(data):
        pass

    
    def layout(worksheet):
        pprint(worksheet)


    dataset = Dataset('Enrollment by School Year')
    dataset.table = 'educ_enrollment_by_year_districts'
    dataset.munger = munger
    dataset.layout = layout
    dataset.accept_propogations = False

    return dataset
