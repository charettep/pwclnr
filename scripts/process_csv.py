import os
import pandas as pd
import logging
from scripts.file_operations import save_csv
from scripts.exact_dupl import remove_exact_duplicates
from scripts.domain_dupl import remove_domain_based_duplicates
from scripts.url_cleaning import clean_urls_in_df, count_occurrences
from scripts.logging_utils import log_removed_rows

"""
Main processing logic. Reads the CSV file, removes duplicates, cleans URLs, logs the process,
and outputs the cleaned CSV and the removed rows log.
"""

# Ensure the logs directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/processing.log"),
        logging.StreamHandler()
    ]
)

def process_csv(file_path, clean_urls_flag=True):
    """
    Process the CSV file by removing duplicates and cleaning URLs.

    Steps:
      1. Load CSV with UTF-8-SIG.
      2. Remove exact duplicates.
      3. Log exact duplicates.
      4. Remove domain-based duplicates.
      5. Log domain-based duplicates.
      6. Optionally clean URLs.
      7. Save cleaned DataFrame including the Domain column.

    Args:
        file_path (str): The input CSV file path.
        clean_urls_flag (bool): Whether to clean URLs.

    Returns:
        tuple: (cleaned_file_path, removed_rows_file_path)
    """
    try:
        logging.info(f"Starting to process file: {file_path}")

        # Load the CSV file
        df = pd.read_csv(file_path, encoding="utf-8-sig")

        # Remove exact duplicates
        df, exact_duplicates = remove_exact_duplicates(df)
        removed_rows_file = log_removed_rows(exact_duplicates, "Exact duplicate", "E001")
        logging.info(f"Removed {len(exact_duplicates)} exact duplicates.")

        # Remove domain-based duplicates
        df, domain_duplicates = remove_domain_based_duplicates(df)
        removed_rows_file = log_removed_rows(domain_duplicates, "Domain-based duplicate", "E002", add_domain=True)
        logging.info(f"Removed {len(domain_duplicates)} domain-based duplicates.")

        if clean_urls_flag:
            # Count occurrences before cleaning (optional)
            count_www_before = count_occurrences(df, 'www.')
            count_http_before = count_occurrences(df, 'http://')
            count_https_before = count_occurrences(df, 'https://')

            # Clean URLs in the DataFrame
            df = clean_urls_in_df(df)
            logging.info("Cleaned URLs by removing 'www.', 'http://', and 'https://'.")

            # Count occurrences after cleaning (optional)
            count_www_after = count_occurrences(df, 'www.')
            count_http_after = count_occurrences(df, 'http://')
            count_https_after = count_occurrences(df, 'https://')

            removed_www = count_www_before - count_www_after
            removed_http = count_http_before - count_http_after
            removed_https = count_https_before - count_https_after

            logging.info(f"Removed {removed_www} occurrences of 'www.'.")
            logging.info(f"Removed {removed_http} occurrences of 'http://'.")
            logging.info(f"Removed {removed_https} occurrences of 'https://'.")

        # Save the cleaned CSV, including the Domain column.
        cleaned_file = save_csv(df, "cleaned_file.csv")
        logging.info(f"Processing completed successfully. Cleaned File: {cleaned_file}")

        return cleaned_file, removed_rows_file

    except Exception as e:
        logging.exception(f"An error occurred while processing the file: {e}")
        raise