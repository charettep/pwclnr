import pandas as pd
from scripts.utils import extract_domain

"""
Handles removal of domain-based duplicates from the DataFrame.
"""

def remove_domain_based_duplicates(df):
    """
    Remove domain-based duplicates from the DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.

    Returns:
        tuple: (DataFrame without domain-based duplicates, DataFrame of removed domain-based duplicates)
    """
    df['Domain'] = df['url'].apply(lambda x: extract_domain(x) if isinstance(x, str) else x)
    domain_duplicates = df[df.duplicated(subset=["Domain", "username", "password"], keep=False)]
    df = df.drop_duplicates(subset=["Domain", "username", "password"], keep='first')
    return df, domain_duplicates