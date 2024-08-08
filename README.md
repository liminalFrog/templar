# Templar
A simple receipt and invoice scanning, using Tesseract, for quick CSV creation
## Installation
Download files and `cd` into the directory using the terminal.  Then install dependencies:
```pip install -r requirements.txt```
## Usage
```python3 main.py -i image-file.jpg```
## Roadmap
-  Export to CSV file
-  Parse out totals, subtotals, tax, and line items
-  Create split transactions for double-entry accounting