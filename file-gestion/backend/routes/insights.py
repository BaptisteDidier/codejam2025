import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype

def get_row(dataframe):
    return len(dataframe), dataframe.index.tolist()

def get_col(dataframe):
    return len(dataframe.columns), dataframe.columns.tolist()
    
def get_missing_vals(dataframe):
    missing_locations = dataframe[dataframe.isna()].stack().index
    return len(missing_locations), missing_locations

#statistics

def get_mean(dataframe, col_name):
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].mean()

def get_median(dataframe, col_name):
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].median()

def get_min(dataframe, col_name):
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].min()

def get_max(dataframe, col_name):
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].max()

def get_mode(dataframe, col_name):
    return dataframe[col_name].mode().tolist()
