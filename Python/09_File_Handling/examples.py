# ============================================================================
#                    FILE HANDLING - CODE EXAMPLES
# ============================================================================

import os
import json
import csv

# Create a test directory for our examples
test_dir = "file_examples"
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# ----------------------------------------------------------------------------
# 1. BASIC FILE OPERATIONS
# ----------------------------------------------------------------------------

print("=== Basic File Operations ===")

# Writing to a file
with open(f"{test_dir}/sample.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is line 2.\n")
    f.write("This is line 3.\n")
print("File written successfully!")

# Reading entire file
with open(f"{test_dir}/sample.txt", "r") as f:
    content = f.read()
    print(f"File content:\n{content}")

# Reading specific number of characters
with open(f"{test_dir}/sample.txt", "r") as f:
    first_10 = f.read(10)
    print(f"First 10 characters: '{first_10}'")


# ----------------------------------------------------------------------------
# 2. READING LINE BY LINE
# ----------------------------------------------------------------------------

print("\n=== Reading Line by Line ===")

# Using readline()
with open(f"{test_dir}/sample.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")

# Using readlines()
with open(f"{test_dir}/sample.txt", "r") as f:
    lines = f.readlines()
    print(f"All lines as list: {lines}")

# Iterating (most memory efficient)
print("\nIterating through file:")
with open(f"{test_dir}/sample.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Line {i}: {line.strip()}")


# ----------------------------------------------------------------------------
# 3. WRITING MODES
# ----------------------------------------------------------------------------

print("\n=== Writing Modes ===")

# Write mode (overwrites)
with open(f"{test_dir}/write_test.txt", "w") as f:
    f.write("First write\n")

with open(f"{test_dir}/write_test.txt", "w") as f:
    f.write("Second write - overwrites!\n")

with open(f"{test_dir}/write_test.txt", "r") as f:
    print(f"After 'w' mode: {f.read().strip()}")

# Append mode
with open(f"{test_dir}/append_test.txt", "w") as f:
    f.write("Line 1\n")

with open(f"{test_dir}/append_test.txt", "a") as f:
    f.write("Line 2 - appended!\n")

with open(f"{test_dir}/append_test.txt", "r") as f:
    print(f"After 'a' mode:\n{f.read()}")


# ----------------------------------------------------------------------------
# 4. WRITELINES
# ----------------------------------------------------------------------------

print("=== Writelines ===")

lines = ["Apple\n", "Banana\n", "Cherry\n"]
with open(f"{test_dir}/fruits.txt", "w") as f:
    f.writelines(lines)

with open(f"{test_dir}/fruits.txt", "r") as f:
    print(f"Written lines: {f.readlines()}")


# ----------------------------------------------------------------------------
# 5. FILE POSITION (seek and tell)
# ----------------------------------------------------------------------------

print("\n=== File Position ===")

with open(f"{test_dir}/sample.txt", "r") as f:
    print(f"Initial position: {f.tell()}")

    content = f.read(5)
    print(f"Read 5 chars: '{content}'")
    print(f"Position after read: {f.tell()}")

    f.seek(0)  # Go back to beginning
    print(f"Position after seek(0): {f.tell()}")

    f.seek(0, 2)  # Go to end
    print(f"Position at end: {f.tell()}")


# ----------------------------------------------------------------------------
# 6. READ AND WRITE MODE
# ----------------------------------------------------------------------------

print("\n=== Read and Write Mode (r+) ===")

# Create file first
with open(f"{test_dir}/rw_test.txt", "w") as f:
    f.write("Original content here")

# Read and write
with open(f"{test_dir}/rw_test.txt", "r+") as f:
    content = f.read()
    print(f"Original: {content}")

    f.seek(0)
    f.write("Modified")
    f.seek(0)
    print(f"After modification: {f.read()}")


# ----------------------------------------------------------------------------
# 7. WORKING WITH PATHS
# ----------------------------------------------------------------------------

print("\n=== Working with Paths (os module) ===")

print(f"Current directory: {os.getcwd()}")
print(f"Files in test_dir: {os.listdir(test_dir)}")
print(f"sample.txt exists: {os.path.exists(f'{test_dir}/sample.txt')}")
print(f"Is file: {os.path.isfile(f'{test_dir}/sample.txt')}")
print(f"Is directory: {os.path.isdir(test_dir)}")

# Path joining (cross-platform)
path = os.path.join(test_dir, "subfolder", "file.txt")
print(f"Joined path: {path}")

# Get file info
stat_info = os.stat(f"{test_dir}/sample.txt")
print(f"File size: {stat_info.st_size} bytes")


# ----------------------------------------------------------------------------
# 8. PATHLIB (Modern approach)
# ----------------------------------------------------------------------------

print("\n=== Pathlib (Modern approach) ===")

from pathlib import Path

p = Path(f"{test_dir}/sample.txt")
print(f"Path: {p}")
print(f"Name: {p.name}")
print(f"Suffix: {p.suffix}")
print(f"Stem: {p.stem}")
print(f"Parent: {p.parent}")
print(f"Exists: {p.exists()}")

# Read and write with pathlib
p = Path(f"{test_dir}/pathlib_test.txt")
p.write_text("Hello from pathlib!")
print(f"Content: {p.read_text()}")


# ----------------------------------------------------------------------------
# 9. CSV FILES
# ----------------------------------------------------------------------------

print("\n=== CSV Files ===")

# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open(f"{test_dir}/data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
print("CSV written!")

# Reading CSV
print("\nReading CSV:")
with open(f"{test_dir}/data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

# DictReader and DictWriter
print("\nUsing DictReader:")
with open(f"{test_dir}/data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['Name']} is {row['Age']} years old")


# ----------------------------------------------------------------------------
# 10. JSON FILES
# ----------------------------------------------------------------------------

print("\n=== JSON Files ===")

# Writing JSON
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "languages": ["Python", "JavaScript", "Go"],
    "employed": True
}

with open(f"{test_dir}/data.json", "w") as f:
    json.dump(data, f, indent=4)
print("JSON written!")

# Reading JSON
with open(f"{test_dir}/data.json", "r") as f:
    loaded = json.load(f)
print(f"Loaded JSON: {loaded}")
print(f"Name: {loaded['name']}")
print(f"Languages: {loaded['languages']}")

# JSON string operations
json_string = json.dumps(data)
print(f"\nJSON string: {json_string[:50]}...")

parsed = json.loads(json_string)
print(f"Parsed back: {parsed['name']}")


# ----------------------------------------------------------------------------
# 11. BINARY FILES
# ----------------------------------------------------------------------------

print("\n=== Binary Files ===")

# Writing binary
binary_data = bytes([0, 1, 2, 3, 255, 254, 253])
with open(f"{test_dir}/binary.bin", "wb") as f:
    f.write(binary_data)
print(f"Written binary data: {binary_data}")

# Reading binary
with open(f"{test_dir}/binary.bin", "rb") as f:
    read_data = f.read()
print(f"Read binary data: {read_data}")
print(f"As list: {list(read_data)}")


# ----------------------------------------------------------------------------
# 12. PRACTICAL EXAMPLES
# ----------------------------------------------------------------------------

print("\n=== Practical Examples ===")

# Example 1: Count lines, words, characters
def file_stats(filename):
    with open(filename, "r") as f:
        content = f.read()
        lines = content.count("\n") + (1 if content and not content.endswith("\n") else 0)
        words = len(content.split())
        chars = len(content)
        return lines, words, chars

lines, words, chars = file_stats(f"{test_dir}/sample.txt")
print(f"sample.txt stats: {lines} lines, {words} words, {chars} characters")


# Example 2: Search in file
def search_in_file(filename, search_term):
    results = []
    with open(filename, "r") as f:
        for i, line in enumerate(f, 1):
            if search_term.lower() in line.lower():
                results.append((i, line.strip()))
    return results

results = search_in_file(f"{test_dir}/sample.txt", "line")
print(f"\nSearch results for 'line': {results}")


# Example 3: Copy file
def copy_file(src, dst):
    with open(src, "r") as source:
        with open(dst, "w") as dest:
            dest.write(source.read())

copy_file(f"{test_dir}/sample.txt", f"{test_dir}/sample_copy.txt")
print(f"File copied!")


# Example 4: Merge files
def merge_files(file_list, output_file):
    with open(output_file, "w") as out:
        for filename in file_list:
            with open(filename, "r") as f:
                out.write(f"--- {filename} ---\n")
                out.write(f.read())
                out.write("\n")

merge_files(
    [f"{test_dir}/sample.txt", f"{test_dir}/fruits.txt"],
    f"{test_dir}/merged.txt"
)
print("Files merged!")


# Example 5: Log file handler
class SimpleLogger:
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def read_logs(self):
        try:
            with open(self.filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            return "No logs yet"

logger = SimpleLogger(f"{test_dir}/app.log")
logger.log("Application started")
logger.log("Processing data...")
logger.log("Application finished")
print(f"\nLog contents:\n{logger.read_logs()}")


# Cleanup (optional - comment out to keep files)
# import shutil
# shutil.rmtree(test_dir)
# print(f"\nCleaned up {test_dir}/")

print("\n=== File Handling Examples Complete ===")
