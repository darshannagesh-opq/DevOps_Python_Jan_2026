# ------------------------------------------------------------
# FILE HANDLING IN PYTHON
# ------------------------------------------------------------
# Files are of two types:
# 1. Text files   → .txt, .csv, .json, .py
# 2. Binary files → .jpg, .png, .mp3, .pdf
#
# File handling allows us to:
# - Open a file
# - Read data
# - Write data
# - Append data
# - Move cursor
# - Work in different modes (r, w, a, r+, w+, a+)
# ------------------------------------------------------------


# ------------------------------------------------------------
# OPENING A FILE
# Syntax: open("filepath", "mode")
# ------------------------------------------------------------

# file = open("sample.txt", "r")

# Always close the file after use:
# file.close()


# ------------------------------------------------------------
# READ ENTIRE FILE
# read()
# ------------------------------------------------------------

# file = open("sample.txt", "r")
# data = file.read()
# print(data)
# file.close()

# Explanation:
# read() → reads the whole file content as a single string.


# ------------------------------------------------------------
# read(n) → read first n characters
# ------------------------------------------------------------

# file = open("sample.txt", "r")
# data = file.read(5)
# print(data)
# file.close()

# Explanation:
# If file contains "Hello Students",
# read(5) returns "Hello".


# ------------------------------------------------------------
# readline() → reads ONE line at a time
# ------------------------------------------------------------

# file = open("sample.txt", "r")
# print(file.readline())  # line 1
# print(file.readline())  # line 2
# print(file.readline())  # line 3
# file.close()

# Explanation:
# Useful for reading line-by-line (especially large files).


# ------------------------------------------------------------
# readlines() → reads ALL lines as a list
# ------------------------------------------------------------

# file = open("sample.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()

# Explanation:
# If file has 3 lines, result will be:
# ["line1\n", "line2\n", "line3\n"]


# ------------------------------------------------------------
# WRITING TO A FILE
# write()
# ------------------------------------------------------------

# f = open("sample.txt", "w")
# f.write("Hello students\n")
# f.write("Good morning")
# f.close()

# Explanation:
# Mode "w" → overwrites the entire file or creates a new one.


# ------------------------------------------------------------
# writelines() → write multiple lines at once
# ------------------------------------------------------------

# f = open("demo.txt", "w")
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# f.writelines(lines)
# f.close()


# ------------------------------------------------------------
# FILE CURSOR POSITIONING
# seek() → move the cursor
# tell() → shows current position
# ------------------------------------------------------------

# f = open("sample.txt", "r")
# f.seek(5)          # move to 6th character
# print(f.read())    # read from new position
# f.close()

# f = open("sample.txt", "r")
# print(f.tell())    # shows starting position (0)
# f.read(6)
# print(f.tell())    # shows new cursor position
# f.close()


# ------------------------------------------------------------
# USING "with" — Best Practice
# ------------------------------------------------------------
# Automatically closes the file
# ------------------------------------------------------------

# with open("sample.txt", "r") as f:
#     print(f.read())


# ------------------------------------------------------------
# FILE MODES
# ------------------------------------------------------------
# r  → read only (file must exist)
# w  → write only (overwrites file)
# a  → append only (add at end)
# r+ → read + write (does NOT erase file)
# w+ → write + read (erases file first)
# a+ → append + read (cursor starts at end)
# ------------------------------------------------------------


# ------------------------------------------------------------
# r+  → Read + Write
# File must exist
# Overwrites only from writing position
# ------------------------------------------------------------

# with open("sample.txt", "r+") as f:
#     f.write("Start-")   # overwrites first few characters
#     print(f.tell())     # current cursor position
#     f.seek(0)
#     print(f.read())

# Explanation:
# If original file:  HELLO WORLD
# After f.write("Start-"):
# Result:            Start- WORLD
# Only first 6 characters replaced.


# ------------------------------------------------------------
# w+  → Write + Read
# Clears file first
# ------------------------------------------------------------

# with open("sample.txt", "w+") as f:
#     f.write("Python File Handling")
#     print(f.tell())   # cursor at end
#     f.seek(0)
#     print(f.read())


# ------------------------------------------------------------
# a+  → Append + Read
# Cursor starts at END
# ------------------------------------------------------------

# with open("sample.txt", "a+") as f:
#     f.write("\nNew line added")
#     f.seek(0)          # go back to top to read
#     print(f.read())


# ------------------------------------------------------------
# BINARY FILES (images, audio, video)
# ------------------------------------------------------------

# with open("download.png", "rb") as f:
#     data = f.read()
#     print("Size in bytes:", len(data))

# Explanation:
# "rb" → read in binary mode
# Useful for images, PDFs, audio files, etc.


# ------------------------------------------------------------
# MINI LOGGING EXAMPLE USING FILE APPEND
# ------------------------------------------------------------

# from datetime import datetime
# with open("logs.txt", "a") as f:
#     f.write(f"User logged in at {datetime.now()}\n")

# Explanation:
# "a" adds new logs without deleting old ones.