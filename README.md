# SSN Scraper

## Overview

The SSN Scraper is a Python-based tool designed to scan text files, PDFs, and Word documents in a specified directory for Social Security Numbers (SSNs). The tool identifies SSNs using a regular expression pattern and redacts the last six digits of any SSNs found. The results of the scan are saved to a timestamped text file.

## Libraries Used

The SSN Scraper uses the following Python libraries:
- `os`: For directory and file operations.
- `re`: For regular expression matching.
- `docx`: For reading Word documents.
- `PyPDF2`: For reading PDF files.
- `datetime`: For handling date and time.

## Installation

To install the required libraries, you can use `pip`. Run the following commands in your terminal:

```bash
pip install python-docx
pip install PyPDF2
```

## How to Run the Script

1. Clone or download the SSN Scraper script to your local machine.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using Python:

```bash
python ssn_scraper.py
```

The script will scan the current directory and its subdirectories for `.txt`, `.pdf`, and `.docx` files, search for SSNs, redact the last six digits of any SSNs found, and save the results to a timestamped text file.

## Example Output

The output will be saved to a file named `ssn_scan_results_YYYYMMDD_HHMMSS.txt`, where `YYYYMMDD_HHMMSS` represents the date and time when the scan was performed.

```txt
Scan performed on: 2024-06-30 12:34:56

SSNs found in /path/to/file.txt: ['123-XX-XXXX']
SSNs found in /path/to/file.pdf: ['456-XX-XXXX']
No SSNs found in the current folder.
```

The output includes the scan date and time, the file paths where SSNs were found, and the redacted SSNs.
