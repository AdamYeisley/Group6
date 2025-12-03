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

def read_sql(e, q_type: int, p=(None, )):
    match q_type:
        case 1:
            query = """
                    SELECT e.job_title, AVG(e.salary_usd) FROM employee e 
                    JOIN company c ON e.companyID = c.companyID 
                    JOIN country co ON c.countryID = co.countryID 
                    WHERE co.name = %s
                    GROUP BY e.job_title 
                    ORDER BY avg DESC 
                    LIMIT 3
                    """
        case 2:
            query = """
                    SELECT c.size, co.name, AVG(e.salary_usd) FROM company c  
                    JOIN country co ON c.countryID = co.countryID  
                    JOIN employee e ON c.companyID = e.companyID  
                    GROUP BY c.size, co.name  
                    HAVING COUNT(*) > 5  
                    ORDER BY avg DESC 
                    LIMIT 10
                    """
        case 3:
            query ="""
                    SELECT co.name, AVG(e.salary_usd) FROM company c  
                    JOIN country co ON c.countryID = co.countryID  
                    JOIN employee e ON c.companyID = e.companyID  
                    GROUP BY co.name 
                    HAVING COUNT(*) > 5   
                    ORDER BY avg DESC 
                    LIMIT 10
                    """
        case 4:
            query = """
                    SELECT co.name, e.year, AVG(salary_usd) FROM company c
                    JOIN country co on c.countryID = co.countryID 
                    JOIN employee e ON c.companyID = e.companyID
                    WHERE co.name = %s AND e.year >= 2022
                    GROUP BY co.name, e.year
                    ORDER BY co.name, e.year
                    """
        case _:
            query = "None"
    return pd.read_sql(query, e, params=p)

def graphIt(df):
    fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(14,6))

    plt1.bar(df.iloc[:,0], df.iloc[:,1], color='darkviolet', edgecolor='fuchsia', alpha=0.9)
    plt1.set_xlabel('EXP Level', fontsize=12, fontweight='bold')
    plt1.set_ylabel('Average Salary', fontsize=12, fontweight='bold')

    plt2.scatter(df.iloc[:,0], df.iloc[:,1], df.iloc[:,2], color='darkviolet', edgecolor='fuchsia', alpha=0.5)
    plt2.set_xlabel('EXP Level', fontsize=12, fontweight='bold')
    plt2.set_ylabel('Average Salary', fontsize=12, fontweight='bold')
    plt2.set_ylim(0, None)
    plt.close(fig)

    return fig