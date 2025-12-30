import pandas as pd
import re

def clean_column_name(col):
    col = col.strip().upper()
    col = re.sub(r"[^\w]+", "_", col)
    col = re.sub(r"_+", "_", col)
    return col.strip("_")

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [clean_column_name(c) for c in df.columns]
    df = df.where(pd.notnull(df), None)
    return df
