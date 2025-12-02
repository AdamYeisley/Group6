from helper_functions import create_key, merge_df, read_sql
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
from helper_functions import create_key, merge_df, graphIt
import matplotlib.pyplot as plt
import pytest
import pandas as pd

#Test the data_cleaning functions
def test_create_key():
    #Arrange
    df = pd.DataFrame({"key1": [1], "key2": [2]})

    #Act
    result = create_key(df)

    #Assert
    assert result == range(1,2)

def test_merge_df():
    #Arrange
    df1 = pd.DataFrame({"key1": [1, 2, 3, 4], "val1": ["A", "B", "C", "D"]})
    df2 = pd.DataFrame({"key1": [2, 3, 5], "val2": ["X", "Y", "Z"]})
    expected_df = pd.DataFrame({"key1": [1, 2, 3, 4], "val1": ["A", "B", "C", "D"], "val2": [None, "X", "Y", None]})

    #Act
    result = merge_df(df1, df2, ["key1", "val2"], ["key1"], ["key1"])

    #Assert
    pd.testing.assert_frame_equal(result, expected_df)

def test_read_sql_case_1():
    #Arrange
    load_dotenv() 
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)

    expected_df = pd.DataFrame({
        "job_title": ["Data Science Tech Lead", "Head of Machine Learning", "Finance Data Analyst"],
        "avg": [375000.0, 337000.0,	323905.0]
    })

    #Act
    result = read_sql(engine, 1, ("US", ))

    #Assert
    pd.testing.assert_frame_equal(result, expected_df)

def test_read_sql_case_2():
     #Arrange
    load_dotenv() 
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)

    expected_df = pd.DataFrame({
        "size": ["M", "L", "M", "M", "M", "M", "M", "L", "S", "S"],
        "name": ["MX", "US", "US", "NZ", "CA", "EG", "AU", "CH", "CA", "US"],
        "avg": [208987.500000, 163915.671815, 156712.045342, 154015.000000, 149693.092637,
                140869.230769, 138695.209302, 137323.142857, 119045.500000, 114857.164179]
    })

    #Act
    result = read_sql(engine, 2)

    #Assert
    pd.testing.assert_frame_equal(result, expected_df)

def test_read_sql_case_3():
     #Arrange
    load_dotenv() 
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)

    expected_df = pd.DataFrame({
        "name": ["US", "NZ", "CA", "EG", "MX", "AU", "CH", "JP", "UA", "IE"],
        "avg": [156904.423130, 146761.250000, 145918.096703, 140869.230769, 129240.600000,
                127800.701754, 124646.888889, 110821.625000, 105600.000000, 104694.916667]
    })

    #Act
    result = read_sql(engine, 3)

    #Assert
    pd.testing.assert_frame_equal(result, expected_df)
    
#use pytest --mpl
@pytest.mark.mpl_image_compare
def test_graphIt():

    df = pd.DataFrame({"X": ['A', 'B', 'C'], "Y": [10, 20, 15], "Z": [1, 2, 3]})
    figure = graphIt(df)
    return figure
