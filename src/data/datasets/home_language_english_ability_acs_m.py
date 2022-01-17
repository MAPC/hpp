from ..Dataset import Dataset

def home_language_english_ability_acs_m():

    def munger(data):
        pass

    
    def layout(worksheet):
        pass


    dataset = Dataset('Language Spoken at Home with Ability to Speak English')
    dataset.table = 'b16004_home_language_english_ability_acs_m'
    dataset.group = 'demographics'
    dataset.munger = munger
    dataset.layout = layout

    return dataset
