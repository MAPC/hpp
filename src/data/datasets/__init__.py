"""
HPP Datasets

Each dataset is responsible for declaring its own configuration
and mungers. If the dataset set is to be used, the constructor
function should be imported and added to the list of contructors.
"""

from .avg_hhsize_by_tenure_acs_m import avg_hhsize_by_tenure_acs_m
from .costburden_acs_m import costburden_acs_m
from .costburden_by_age_acs_m import costburden_by_age_acs_m
from .costburden_by_income_acs_m import costburden_by_income_acs_m
from .educ_enrollment_by_year_districts import educ_enrollment_by_year_districts
# from .hh_income_acs_m import hh_income_acs_m
from .hu_occupancy_by_tenure_race_acs_m import hu_occupancy_by_tenure_race_acs_m
from .hh_tenure_by_age_acs_m import hh_tenure_by_age_acs_m
from .hh_with_seniors_acs_m import hh_with_seniors_acs_m
from .home_language_english_ability_acs_m import home_language_english_ability_acs_m
from .hous_hh_income_by_cb_chas_m import hous_hh_income_by_cb_chas_m
from .hous_hh_income_by_hh_type_chas_m import hous_hh_income_by_hh_type_chas_m
from .hous_hh_type_by_cb_chas_m import hous_hh_type_by_cb_chas_m
from .hous_hh_type_size_by_seniors_m import hous_hh_type_size_by_seniors_m
# from .hous_res_sales_by_type_value_m import hous_res_sales_by_type_value_m
from .hous_shi_m import hous_shi_m
from .hu_tenure_by_units_acs_m import hu_tenure_by_units_acs_m
from .hu_tenure_year_built_units_acs_m import hu_tenure_year_built_units_acs_m
from .hu_units_in_structure_acs_m import hu_units_in_structure_acs_m
from .mhi_fam_acs_m import mhi_fam_acs_m
from .mhi_tenure_acs_m import mhi_tenure_acs_m
from .population_by_age_gender_acs_m import population_by_age_gender_acs_m
from .poverty_by_hh_type_acs_m import poverty_by_hh_type_acs_m
from .race_ethnicity_acs_m import race_ethnicity_acs_m
from .rent_acs_m import rent_acs_m

data_constructors = [
    avg_hhsize_by_tenure_acs_m,
    costburden_acs_m,
    costburden_by_age_acs_m,
    costburden_by_income_acs_m,
    educ_enrollment_by_year_districts,
    # hh_income_acs_m,
    hu_occupancy_by_tenure_race_acs_m,
    hh_tenure_by_age_acs_m,
    hh_with_seniors_acs_m,
    home_language_english_ability_acs_m,
    hous_hh_income_by_hh_type_chas_m,
    hous_hh_income_by_cb_chas_m,
    hous_hh_type_by_cb_chas_m,
    hous_hh_type_size_by_seniors_m,
    # hous_res_sales_by_type_value_m,
    hous_shi_m,
    hu_tenure_by_units_acs_m,
    hu_tenure_year_built_units_acs_m,
    hu_units_in_structure_acs_m,
    mhi_fam_acs_m,
    mhi_tenure_acs_m,
    population_by_age_gender_acs_m,
    poverty_by_hh_type_acs_m,
    race_ethnicity_acs_m,
    rent_acs_m,
]
