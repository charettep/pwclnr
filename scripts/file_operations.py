"""
Handles file-saving operations to ensure the output is placed in the 'output' directory.
"""

import os

def save_csv(dataframe, file_name):
    """
    Saves the given pandas DataFrame to a CSV file in the 'output' directory.

    Args:
        dataframe (pandas.DataFrame): The DataFrame to be exported.
        file_name (str): The name of the CSV file (e.g., 'cleaned_file.csv').

    Returns:
        str: The full path to the saved CSV file.
    """
    # Define the output directory name
    output_dir = "output"
    # Create the output directory if it doesn't already exist
    os.makedirs(output_dir, exist_ok=True)

    # Build the full file path
    file_path = os.path.join(output_dir, file_name)

    # Export the DataFrame to CSV without including the index
    dataframe.to_csv(file_path, index=False)

    # Return this path so other code knows where the file was saved
    return file_path
