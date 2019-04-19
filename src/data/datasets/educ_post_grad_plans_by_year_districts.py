from ..Dataset import Dataset

def educ_post_grad_plans_by_year_districts():

    def munger(data):
        pass

    def layout(worksheet):
        pass

    dataset = Dataset('educ_post_grad_plans_by_year_districts')
    dataset.table = 'educ_post_grad_plans_by_year_districts'
    dataset.group = 'demographics'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
