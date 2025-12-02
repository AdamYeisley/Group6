import pandas as pd
import matplotlib.pyplot as plt

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

def graphIt(df):
    fig, (plt1, plt2) = plt.subplots(2, 1, figsize=(6, 8))

    plt1.bar(df.iloc[:,0], df.iloc[:,1])
    plt1.set_xlabel(df.iloc[:,0].name)
    plt1.set_ylabel(df.iloc[:,1].name)

    plt2.scatter(df.iloc[:,0], df.iloc[:,1], df.iloc[:,2])
    plt2.set_xlabel(df.iloc[:,0].name)
    plt2.set_ylabel(df.iloc[:,1].name)
    plt2.set_ylim(0, None)
    plt.close(fig)

    return fig