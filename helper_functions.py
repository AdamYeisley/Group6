import pandas as pd

#For data_cleaning.ipynb
def create_key(df_to_key: pd.DataFrame):
    return range(1, len(df_to_key) + 1)

def merge_df(df1: pd.DataFrame, df2: pd.DataFrame, join_cols: list, left_common_columns: list, right_common_columns: list):
    return_df = df1.merge(
    df2[join_cols],
    left_on=left_common_columns,
    right_on=right_common_columns,
    how="left"
    )   
    return return_df