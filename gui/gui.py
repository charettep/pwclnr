"""
This file contains all the logic for the graphical user interface (GUI).
It uses Python's tkinter library to provide a window that allows users
to select a CSV file and run the cleaning process.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
# Updated import to use process_csv from the new module
from scripts.process_csv import process_csv  

def launch_gui():
    """
    Launches the main GUI window, which allows the user to select a file
    and start the CSV processing workflow.
    """

    def select_file():
        """
        Opens a file dialog so the user can pick a CSV file. Once a file
        is chosen, the label is updated, and the 'Start' button becomes enabled.
        """
        file_path = filedialog.askopenfilename(
            title="Select a CSV File",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))  # Filter for CSV files primarily
        )
        if file_path:
            # Update the label to show which file was selected
            file_label.config(text=f"Selected: {file_path}")
            # Enable the 'Start' button
            run_button.config(state="normal")
            # Store the selected file path in the function object so it can be accessed later
            select_file.selected_file = file_path

    def start_processing():
        """
        When the user clicks 'Start', checks if a file was selected. If so,
        calls process_csv to clean the file, then shows a message on success or error.
        """
        # If no file has been selected, display an error message
        if not hasattr(select_file, 'selected_file'):
            messagebox.showerror("Error", "Please select a file first.")
            return
        try:
            # Call our logic function to process the chosen CSV
            cleaned_file, removed_rows_file = process_csv(select_file.selected_file, clean_urls_var.get())
            # Display a message to let the user know it finished successfully
            messagebox.showinfo("Success", f"Processing complete!\n\nCleaned file: {cleaned_file}\nRemoved rows file: {removed_rows_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Create the main window
    root = tk.Tk()
    root.title("CSV Password Cleaner")  # Set the window title

    # Create a button that triggers the select_file() function
    select_button = tk.Button(root, text="Select CSV File", command=select_file)
    select_button.pack(pady=10)

    # Create a label that displays the currently selected file
    file_label = tk.Label(root, text="No file selected.")
    file_label.pack(pady=5)

    # Add checkboxes for configuration options
    clean_urls_var = tk.BooleanVar(value=True)
    clean_urls_checkbox = tk.Checkbutton(root, text="Clean URLs", variable=clean_urls_var)
    clean_urls_checkbox.pack(pady=5)

    # Add a progress bar
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=10)

    # Create a 'Start' button to initiate the process
    # Initially disabled, it becomes enabled once a file is selected
    run_button = tk.Button(root, text="Start", command=start_processing, state="disabled")
    run_button.pack(pady=10)

    # Begin the Tkinter event loop, which listens for user actions
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
