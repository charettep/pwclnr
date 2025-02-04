# CSV Password Cleaner 🚀

License: MIT

## Overview

PWCLNR is a robust Python CSV Password Cleaner application to consolidates CSV passwords exports from various password managers to migrate into a single new password manager, without duplicates entries. It removes duplicates and normalizes URLs, proven to work efficiently on files with up to 30,000 lines. Running locally ensures privacy while handling critical personal information.

## Features

- **Duplicate Removal:** Eliminates exact duplicate rows based on URL, username, and password.
- **Domain Handling:** Identifies and removes duplicates on a domain basis.
- **URL Standardization:** Cleans URLs by stripping prefixes like 'www.', 'http://', and 'https://'.
- **Logging:** Generates a detailed log of the cleaning process including counts of removed duplicates and URL occurrences.
- **Output Generation:** Produces two output files:
  - `cleaned_file.csv`: The cleaned CSV file.
  - `removed_rows.csv`: The log CSV file detailing rows removed during processing.
- **Graphical User Interface (GUI):** Built using tkinter for easy file selection and operation.
- **CLI Entry-Point:** The application launches via `main.py` which starts the GUI.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Development](#development)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/charettep/pwclnr.git
   cd pwclnr
   ```

2. **Set Up the Environment:**
   Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your CSV File:**
   Use template.csv provided in /input as a reference to structure your CSV file. Ensure your CSV contains columns for URL, username, and password.

2. **Run the Application:**
   Execute the following command to clean your CSV:

   ```bash
   python main.py --input <YOURINPUTFILENAME>.csv --output cleaned_file.csv
   ```

   This will remove duplicate records, standardize URLs, and generate a log file detailing the process.

3. **Explore the GUI (Optional):**
   For a graphical interface, run:

   ```bash
   python gui.py
   ```

## Configuration

Adjust cleaning parameters or log settings directly within the source code. Inline comments provide guidance on how to modify the configurations to suit your needs.

## Development

To contribute to the development of this project, follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Implement your changes with clear commit messages.
4. Push your branch.
5. Open a pull request.

For more details, please review [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the software according to the license terms.

## Acknowledgements

Special thanks to all contributors and the open source community. Built with ❤️ using Python, pandas, and tldextract.

Happy Cleaning! 🧹
