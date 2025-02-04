import pandas as pd

"""
Handles removal of exact duplicates from the DataFrame.
"""

def remove_exact_duplicates(df):
    """
    Remove exact duplicates based on url, username, and password.

    Args:
        df (pandas.DataFrame): The DataFrame to process.

    Returns:
        tuple: (DataFrame without exact duplicates, DataFrame of removed exact duplicates)
    """
    exact_duplicates = df[df.duplicated(subset=["url", "username", "password"], keep=False)]
    df = df.drop_duplicates(subset=["url", "username", "password"])
    return df, exact_duplicates