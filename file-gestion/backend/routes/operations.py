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

def change(dataframe, row_name, col_name, value):
    if row_name not in dataframe.index:
        raise ValueError(f"Row '{row_name}' does not exist in the DataFrame.")
    if col_name not in dataframe.columns:
        raise ValueError(f"Column '{col_name}' does not exist in the DataFrame.")
    dataframe.loc[row_name, col_name] = value
    return dataframe

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

# File Operations
def save_csv(dataframe, filename):
    dataframe.to_csv(filename, index=True)
    return filename
