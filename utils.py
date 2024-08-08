import pandas as pd

def add_column(df: pd.DataFrame, column_name: str, data: list) -> pd.DataFrame:
    df[column_name] = data
    return df

def remove_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df = df.drop(columns=[column_name])
    return df

def filter_rows(df: pd.DataFrame, condition) -> pd.DataFrame:
    filtered_df = df[df.apply(condition, axis=1)]
    return filtered_df

def rename_columns(df: pd.DataFrame, columns_name: str) -> pd.DataFrame:
    df = df.rename(columns=columns_name)
    return df

def sum_column(df: pd.DataFrame, column_name) -> float:
    total = df[column_name].sum()
    return total




