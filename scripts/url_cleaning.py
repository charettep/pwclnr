import pandas as pd

"""
Handles URL cleaning operations.
"""

def clean_urls_in_df(df):
    """
    Clean the URLs in the DataFrame by removing 'http://', 'https://', and 'www.'.

    Args:
        df (pandas.DataFrame): The DataFrame to process.

    Returns:
        pandas.DataFrame: The DataFrame with cleaned URLs.
    """
    df['url'] = df['url'].apply(
        lambda x: x.replace('http://', '')
                   .replace('https://', '')
                   .replace('www.', '')
        if isinstance(x, str) else x
    )
    return df

def count_occurrences(df, substr):
    """
    Count the number of occurrences of a substring in the 'url' column of a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the 'url' column.
        substr (str): The substring to count.

    Returns:
        int: The number of occurrences of the substring.
    """
    return df['url'].apply(lambda x: x.count(substr) if isinstance(x, str) else 0).sum()