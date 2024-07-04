import numpy as np
import pandas as pd
import pytest
from identity_voting.config import TEST_DIR
from identity_voting.data_management.clean_data import extract_non_na_values



def test_extract_non_na_values():
    # Test case 1: Each row has exactly one non-NA value, including 'NaN' strings
    df1 = pd.DataFrame({
        'Closest_Political_Party_Germany': [np.nan, 'NaN', np.nan, np.nan, np.nan],
        'Closest_Political_Party_Austria': [1.0, 5.0, 'NaN', 66.0, 5.0]
    })
    result1 = extract_non_na_values(df1)
    expected1 = pd.Series([1.0, 5.0, np.nan, 66.0, 5.0])
    pd.testing.assert_series_equal(result1, expected1)
    
    # Test case 2: Some rows have all NA values, including 'NaN' strings
    df2 = pd.DataFrame({
        'Closest_Political_Party_Germany': [np.nan, 2.0, np.nan],
        'Closest_Political_Party_Austria': ['NaN', np.nan, 3.0]
    })
    result2 = extract_non_na_values(df2)
    expected2 = pd.Series([np.nan, 2.0, 3.0])
    pd.testing.assert_series_equal(result2, expected2)
    
    # Test case 3: All rows have the same non-NA value column
    df3 = pd.DataFrame({
        'Closest_Political_Party_Germany': [7.0, 7.0, 7.0],
        'Closest_Political_Party_Austria': [np.nan, 'NaN', np.nan]
    })
    result3 = extract_non_na_values(df3)
    expected3 = pd.Series([7.0, 7.0, 7.0])
    pd.testing.assert_series_equal(result3, expected3)
    
    # Test case 4: Mixed NA and non-NA values, including 'NaN' strings
    df4 = pd.DataFrame({
        'Col1': [np.nan, 'NaN', 2.0, np.nan],
        'Col2': [3.0, np.nan, 'NaN', np.nan],
        'Col3': [np.nan, 1.0, np.nan, 4.0]
    })
    result4 = extract_non_na_values(df4)
    expected4 = pd.Series([3.0, 1.0, 2.0, 4.0])
    pd.testing.assert_series_equal(result4, expected4)