Disk Sanitiser

📌 Description

Disk Sanitiser is a Python-based utility that scans a specified directory, identifies duplicate files using MD5 checksums, and removes duplicate copies while keeping one original file.

The program also generates a detailed log report containing scan information, duplicate files, deleted files, and execution time.

🚀 Features

- Scans files recursively inside a directory
- Calculates MD5 checksum for each file
- Detects files with identical content
- Deletes duplicate copies while keeping one file
- Generates a timestamped duplicate file report
- Displays a summary after execution
- Measures total execution time

🛠️ Technologies Used

- Python 3
- "os"
- "sys"
- "hashlib"
- "time"
- "datetime"

▶️ How to Run

Open the terminal in the project directory and run:

python DiskSanitiser.py "DirectoryPath"

Example

python DiskSanitiser.py "D:\TestFolder"

📄 Log Report

After execution, the program creates a timestamped log file.

The report contains:

- Scan date and time
- Directory scanned
- Total files scanned
- Number of duplicate groups
- List of duplicate files
- Total files deleted
- Total execution time

⚠️ Important Note

This program permanently deletes duplicate files. Always test the program on a sample directory before using it on important data.

👨‍💻 Author

Yash Chavan

📌 Project

Disk Sanitiser – Duplicate File Detection and Removal Utility

Built using Python.