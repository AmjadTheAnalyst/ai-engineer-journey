"""📁 The Challenge: 
Clean the Server LogsImagine you are managing an application server. 
The server tracks every user action in a raw Python list. 
However, because of a network glitch, some actions were logged multiple times in a row, 
and some logs contain messy white spaces.
Your goal is to process this raw list using a for loop to extract only unique, 
cleaned filenames that users accessed."""

raw_logs = [
    "report.csv ", 
    "Data.json", 
    "report.csv", 
    "image.png", 
    "data.json ", 
    "REPORT.CSV", 
    "image.png"
]
cleaned_files = set() 
for file in raw_logs:
    clean_name = file.strip().lower()
    cleaned_files.add(clean_name)
print(cleaned_files)