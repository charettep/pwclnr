import os
import pandas as pd
from scripts.utils import extract_domain

"""
Provides utilities to log removed rows to a CSV file.
"""

def log_removed_rows(removed_rows, reason, error_code, add_domain=True):
    """
    Logs the removed rows to a CSV file with the following columns (in order):
        url, username, password, Domain, ErrorCode, Reason

    The header will be included if the file does not exist. The Domain column is always extracted
    from the URL irrespective of the 'add_domain' flag.

    Args:
        removed_rows (pandas.DataFrame): The rows that were removed.
        reason (str): The reason for removal (which may be based on error type).
        error_code (str): The error code corresponding to the removal reason.
        add_domain (bool): (Ignored; domain is always extracted.)

    Returns:
        str: Path to the removed rows CSV file.
    """
    # Add error code and reason to every row
    removed_rows['ErrorCode'] = error_code
    removed_rows['Reason'] = reason

    # Always extract the domain from the URL
    removed_rows['Domain'] = removed_rows['url'].apply(lambda x: extract_domain(x) if isinstance(x, str) else '')

    # Reorder columns as: url, username, password, Domain, ErrorCode, Reason
    removed_rows = removed_rows[['url', 'username', 'password', 'Domain', 'ErrorCode', 'Reason']]

    # Ensure the output directory exists
    os.makedirs('output', exist_ok=True)

    removed_file = os.path.join('output', 'removed_rows.csv')
    if os.path.exists(removed_file):
        removed_rows.to_csv(removed_file, mode='a', header=False, index=False)
    else:
        removed_rows.to_csv(removed_file, index=False)

    return removed_file