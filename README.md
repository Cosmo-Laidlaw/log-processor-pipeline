# Log Processor Pipeline
A beginner friendly python project for processing log files 

---

## What It Does

This script:
- Reads raw '.txt' log files
- Counts how many lines contain 'SUCCESS' and 'ERROR'
- Extracts all 'ERROR' lines into a separate '.txt' file
- Writes a summary report to a 'json' file
- Handle missing files and exceptions

## Project Structure
log_processor/
├── logs/
│ └── sample_log.txt # Example input log file
├── output/
│ ├── summary.json # Summary of success/error counts
│ └── errors_only.txt # Extracted error lines
├── log_processor.py # Main script
└── README.md # You're reading it!

## How to use it

### Prepare a log file

Your log file should contain lines like:
SUCCESS: Loaded file A
ERROR: Failed to process file B
SUCCESS: Export complete

Save it as `logs/sample_log.txt`

---

### Run the script

From the terminal:

```bash
python log_processor.py
```

### Example output
summary.json

json
{
  "success_count": 4,
  "error_count": 2
}

errors_only.txt

ERROR: Failed to connect
ERROR: Timeout during load

### Features Covered
- File Reading
- JSON handling
- Functions and modular code
- Error Handling with try/except
- Case-insensitive text processing
- CLI-friendly folder structure

### Built with 
- Python 3.x
- VS Code
- Data Engineering principles

### Author
Cosmo Laidlaw
https://github.com/Cosmo-Laidlaw

