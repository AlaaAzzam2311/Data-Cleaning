from learntools.core import binder
binder.bind(globals())
from learntools.data_cleaning.ex1 import *
print("Setup Complete")
# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
sf_permits = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0) 
sf_first_5 = sf_permits.head(5)
print(sf_first_5)

total_length = np.product(sf_permits.shape)
missing_values = sf_permits.isnull().sum().sum()
percent_missing = (missing_values/total_length) * 100
# get the number of missing data points per column
missing_values_count = sf_permits.isnull().sum()

# how many total missing values do we have?
total_cells = np.product(sf_permits.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
sf_permits = sf_permits.dropna()
sf_permits.shape

# remove all columns with at least one missing value
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)
cols_in_original_dataset = sf_permits.shape[1]
cols_in_na_dropped = sf_permits_with_na_dropped.shape[1]
dropped_columns = cols_in_original_dataset - cols_in_na_dropped

sf_permits_with_na_imputed = sf_permits.fillna(method='bfill', axis=0).fillna(0)
