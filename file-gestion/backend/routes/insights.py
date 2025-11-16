import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
from fastapi import APIRouter, HTTPException, JSONResponse
from fastapi.responses import FileResponse
import os

# Data Cleaning / Transformation
def drop_row(dataframe, row_index):
    if row_index not in dataframe.index:
        raise ValueError(f"Row '{row_index}' does not exist in the DataFrame.")
    dataframe = dataframe.drop(index=row_index)
    return dataframe

def drop_col(dataframe, col_name):
    if col_name not in dataframe.columns:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    dataframe = dataframe.drop(columns=col_name)
    return dataframe

def fill_missing(dataframe, col_name, value):
    if col_name not in dataframe.columns:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    dataframe[col_name] = dataframe[col_name].fillna(value)
    return dataframe

def rename_col(dataframe, old_name, new_name):
    if old_name not in dataframe.columns:
        raise ValueError(f"Column '{old_name}' does not exist in the DataFrame.")
    dataframe = dataframe.rename(columns={old_name: new_name})
    return dataframe

def drop_duplicates(dataframe, subset=None):
    if subset:
        for col in subset:
            if col not in dataframe.columns:
                raise ValueError(f"Column '{col}' does not exist in the DataFrame.")
    return dataframe.drop_duplicates(subset=subset)

def view(dataframe, row_name, col_name):
    if row_name not in dataframe.index:
        raise ValueError(f"Row '{row_name}' does not exist in the DataFrame.")
    if col_name not in dataframe.columns:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    return dataframe.loc[row_name, col_name]

def change(dataframe, row_name, col_name, value):
    if row_name not in dataframe.index:
        raise ValueError(f"Row '{row_name}' does not exist in the DataFrame.")
    if col_name not in dataframe.columns:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    dataframe.loc[row_name, col_name] = value
    return dataframe

def get_rows(dataframe):
    return len(dataframe), dataframe.index.tolist()

def get_cols(dataframe):
    return len(dataframe.columns), dataframe.columns.tolist()
    
def get_missing_vals(dataframe):
    missing_locations = dataframe[dataframe.isna()].stack().index
    return len(missing_locations), missing_locations

#statistics

def get_mean(dataframe, col_name):
    if col_name not in dataframe:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].mean()

def get_median(dataframe, col_name):
    if col_name not in dataframe:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].median()

def get_min(dataframe, col_name):
    if col_name not in dataframe:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].min()

def get_max(dataframe, col_name):
    if col_name not in dataframe:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].max()

def get_mode(dataframe, col_name):
    if col_name not in dataframe:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    return dataframe[col_name].mode().tolist()

def get_variance(dataframe, col_name):
    if col_name not in dataframe:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].var()

def get_std(dataframe, col_name):
    if col_name not in dataframe:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].std()

def get_covariance(dataframe, col1_name, col2_name):
    if col1_name not in dataframe:
        raise ValueError(f"Column '{col1_name}' does not exist in the DataFrame.")
    if col2_name not in dataframe:
        raise ValueError(f"Column '{col2_name}' does not exist in the DataFrame.")
    
    if not is_numeric_dtype(dataframe[col1_name]):
        raise TypeError(f"Column '{col1_name}' is not numeric.")
    if not is_numeric_dtype(dataframe[col2_name]):
        raise TypeError(f"Column '{col2_name}' is not numeric.")
    
    return dataframe[col1_name].cov(dataframe[col2_name])


def get_quartiles(dataframe, col_name):
    if col_name not in dataframe.columns:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    Q1 = dataframe[col_name].quantile(0.25)
    Q2 = dataframe[col_name].quantile(0.5)
    Q3 = dataframe[col_name].quantile(0.75)
    return Q1, Q2, Q3

def get_range(dataframe, col_name):
    if col_name not in dataframe.columns:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[col_name]):
        raise TypeError(f"Column '{col_name}' is not numeric.")
    return dataframe[col_name].max() - dataframe[col_name].min()

#Filtering
def filter_rows(dataframe, condition_func):
    """
    condition_func: a function that takes the DataFrame and returns a boolean Series
    """
    filtered = dataframe[condition_func(dataframe)]
    return filtered

def filter_cols(dataframe, col_list):
    for col in col_list:
        if col not in dataframe.columns:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame.")
    filtered = dataframe[col_list]
    return filtered

#applying functions

def apply_col(dataframe, col_name, func):
    if col_name not in dataframe:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    dataframe[col_name] = func(dataframe[col_name])
    return dataframe

def apply_row(dataframe, row_index, func):
    if row_index not in dataframe.index:
        raise ValueError(f"Row '{row_index}' does not exist in the DataFrame.")
    
    row = dataframe.loc[row_index]
    dataframe.loc[row_index] = func(row)
    return dataframe
    
def sort_by_col(dataframe, col_name, ascending=True):
    if col_name not in dataframe:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    
    dataframe = dataframe.sort_values(by=col_name, ascending=ascending)
    return dataframe

def transpose(dataframe):
    dataframe = dataframe.T
    return dataframe

#Joins
def join_inner(df1, df2, on):
    if on not in df1.columns or on not in df2.columns:
        raise ValueError(f"Join key '{on}' must exist in both DataFrames.")
    return df1.merge(df2, on=on, how="inner")

def join_left(df1, df2, on):
    if on not in df1.columns or on not in df2.columns:
        raise ValueError(f"Join key '{on}' must exist in both DataFrames.")
    return df1.merge(df2, on=on, how="left")

def join_right(df1, df2, on):
    if on not in df1.columns or on not in df2.columns:
        raise ValueError(f"Join key '{on}' must exist in both DataFrames.")
    return df1.merge(df2, on=on, how="right")

def join_outer(df1, df2, on):
    if on not in df1.columns or on not in df2.columns:
        raise ValueError(f"Join key '{on}' must exist in both DataFrames.")
    return df1.merge(df2, on=on, how="outer")

def join_cross(df1, df2):
    return df1.merge(df2, how="cross")

def join_on_index(df1, df2):
    return df1.join(df2, how="inner")

def join_multi(df1, df2, on_cols, how="inner"):
    for col in on_cols:
        if col not in df1.columns or col not in df2.columns:
            raise ValueError(f"Join key '{col}' must exist in both DataFrames.")
    return df1.merge(df2, on=on_cols, how=how)

#Regression
def fit_linear_regression(dataframe, x_name, y_name):
    if x_name not in dataframe:
        raise ValueError(f"Column '{x_name}' does not exist in the DataFrame.")
    if y_name not in dataframe:
        raise ValueError(f"Column '{y_name}' does not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[x_name]):
        raise TypeError(f"Column '{x_name}' is not numeric.")
    if not is_numeric_dtype(dataframe[y_name]):
        raise TypeError(f"Column '{y_name}' is not numeric.")
    x = np.array(dataframe[x_name])
    y = np.array(dataframe[y_name])

    x_mean = x.mean()
    y_mean = y.mean()

    cov_xy = np.mean((x - x_mean) * (y - y_mean))
    var_x = np.mean((x - x_mean)**2)

    if var_x == 0:
        raise ValueError(f"Variance of '{x_name}' is zero. Cannot fit regression.")

    b1 = cov_xy / var_x
    b0 = y_mean - b1 * x_mean

    return b0, b1

def fit_multiple_linear_regression(dataframe, x_cols, y_col):
    for col in x_cols + [y_col]:
        if col not in dataframe:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame.")
        if not is_numeric_dtype(dataframe[col]):
            raise TypeError(f"Column '{col}' is not numeric.")

    X = dataframe[x_cols].to_numpy()
    y = dataframe[y_col].to_numpy()

    X = np.column_stack((np.ones(X.shape[0]), X))

    try:
        coeffs = np.linalg.inv(X.T @ X) @ X.T @ y
    except np.linalg.LinAlgError:
        raise ValueError("Matrix is singular; cannot compute regression coefficients.")

    b0 = coeffs[0]
    slopes = coeffs[1:]

    return b0, slopes


def r_squared(dataframe, x_name, y_name):
    if x_name not in dataframe or y_name not in dataframe:
        raise ValueError("One or both columns do not exist in the DataFrame.")
    if not is_numeric_dtype(dataframe[x_name]) or not is_numeric_dtype(dataframe[y_name]):
        raise TypeError("Columns must be numeric.")
    
    x = np.array(dataframe[x_name])
    y = np.array(dataframe[y_name])
    b0, b1 = fit_linear_regression(dataframe, x_name, y_name)
    y_pred = b0 + b1 * x
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    return 1 - ss_res / ss_tot


# File Operations
def save_csv(dataframe, filename):
    dataframe.to_csv(filename, index=True)
    return filename
