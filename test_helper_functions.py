from helper_functions import create_key, merge_df, graphIt
import matplotlib.pyplot as plt

#Imports
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

#use pytest --mpl
@pytest.mark.mpl_image_compare
def test_graphIt():

    df = pd.DataFrame({"X": ['A', 'B', 'C'], "Y": [10, 20, 15], "Z": [1, 2, 3]})
    figure = graphIt(df)
    return figure