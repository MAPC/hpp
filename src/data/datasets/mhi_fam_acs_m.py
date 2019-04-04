from ..Dataset import Dataset

def mhi_fam_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Median Household Income by Family Type')
    dataset.table = 'b19013_b19113_b19202_mhi_fam_acs_m'
    dataset.columns = ['muni_id', 'municipal', 'acs_year', 'mhi', 'mhi_me', 'mhi_f', 'mhi_f_me', 'mhi_nf', 'mhi_nf_me']
    dataset.munger = munger
    dataset.layout = layout

    dataset.add_condition('acs_year', '2012-16')

    return dataset
