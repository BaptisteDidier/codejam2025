import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
from fastapi import APIRouter, HTTPException, JSONResponse
from fastapi.responses import FileResponse
from database import db_pool
import os

router = APIRouter()

@router.get("/download/{file_id}")
async def download_file(file_id: int):
    query = "SELECT filepath, filename FROM uploaded_files WHERE id = $1"
    async with db_pool.acquire() as conn:
        row = await conn.fetchrow(query, file_id)
    if not row:
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(path=row['filepath'], filename=row['filename'])

def get_rows(dataframe):
    return len(dataframe), dataframe.index.tolist()

def get_cols(dataframe):
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

@router.get("/insights/{file_id}")
async def get_file_insights(file_id: int):
    # Fetch file path from database
    query = "SELECT filepath, filename FROM uploaded_files WHERE id = $1"
    async with db_pool.acquire() as conn:
        row = await conn.fetchrow(query, file_id)
    
    if not row:
        raise HTTPException(status_code=404, detail="File not found")
    
    filepath = row['filepath']
    
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File missing on server")
    
    # Read CSV file
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV: {str(e)}")
    
    # Gather insights
    insights = {
        "Number of rows": get_rows(df)[0],
        "Rows": get_rows(df)[1],
        "Number of columns": get_cols(df)[0],
        "Columns": get_cols(df)[1],
        "Number of missing values": get_missing_vals(df)[0],
        "Missing values locations": get_missing_vals(df)[1],
        "columns_info": {}
    }
    
    for col in df.columns:
        col_info = {}
        if is_numeric_dtype(df[col]):
            col_info["mean"] = get_mean(df, col)
            col_info["median"] = get_median(df, col)
            col_info["min"] = get_min(df, col)
            col_info["max"] = get_max(df, col)
            col_info["mode"] = get_mode(df, col)
        else:
            col_info["mode"] = get_mode(df, col)
        insights["columns_info"][col] = col_info
    
    return JSONResponse(insights)
