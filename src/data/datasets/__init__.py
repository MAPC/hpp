"""
HPP Datasets

Each dataset is responsible for declaring its own configuration
and mungers. If the dataset set is to be used, the constructor
function should be imported and added to the list of contructors.
"""

from .avg_hhsize_by_tenure_acs_m import avg_hhsize_by_tenure_acs_m

data_constructors = [
    avg_hhsize_by_tenure_acs_m,
]
