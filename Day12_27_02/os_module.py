# ------------------------------------------------------------
# OS MODULE 
# ------------------------------------------------------------
# The 'os' module allows Python to interact with the operating system.
# Using this module, we can:
# - Get current directory
# - Change directories
# - Create folders
# - Delete folders
# - Rename files
# - Check if file/folder exists
# - Get size of files
# - Run system commands (like terminal commands)
# ------------------------------------------------------------

import os


# ------------------------------------------------------------
# 1. GET CURRENT WORKING DIRECTORY
# ------------------------------------------------------------

# print(os.getcwd())

# Explanation:
# os.getcwd() → returns the folder where the Python program is running.


# ------------------------------------------------------------
# 2. CHANGE DIRECTORY
# ------------------------------------------------------------

# os.chdir("some_folder")
# print(os.getcwd())

# Explanation:
# os.chdir() → moves Python into a different directory.


# ------------------------------------------------------------
# 3. LIST ALL FILES & FOLDERS
# ------------------------------------------------------------

# items = os.listdir()
# print(items)

# Explanation:
# os.listdir() returns a list of all files and folders
# inside the current working directory.


# ------------------------------------------------------------
# 4. CREATE FOLDERS
# ------------------------------------------------------------

# os.mkdir("New_folder")     # creates a single folder
# os.makedirs("parent/child/grandchild")  # creates nested folders

# Explanation:
# os.mkdir() → only creates one folder.
# os.makedirs() → creates multiple nested folders in one call.


# ------------------------------------------------------------
# 5. REMOVE FOLDERS
# ------------------------------------------------------------

# os.rmdir("New_folder")              # removes only empty folder
# os.removedirs("parent/child/grandchild")  # removes nested empty folders

# Explanation:
# os.rmdir() → removes only an empty single folder.
# os.removedirs() → removes every folder in the path, but ALL must be empty.


# ------------------------------------------------------------
# 6. RENAME FILE OR FOLDER
# ------------------------------------------------------------

# os.rename("demo.txt", "new_name.txt")

# Explanation:
# os.rename(old_name, new_name) → renames file or folder.


# ------------------------------------------------------------
# 7. CHECK IF A FILE/FOLDER EXISTS
# ------------------------------------------------------------

# print(os.path.exists("sample123.txt"))

# Explanation:
# Returns True if file/folder exists, otherwise False.


# ------------------------------------------------------------
# 8. GET SIZE OF A FILE
# ------------------------------------------------------------

# print(os.path.getsize("sample.txt"))

# Explanation:
# Returns size in bytes.


# ------------------------------------------------------------
# 9. RUN TERMINAL/COMMAND-PROMPT COMMANDS
# ------------------------------------------------------------

# print(os.system("dir"))
# print(os.system("ls"))

# Explanation:
# os.system() lets Python run actual OS shell commands.
# Very useful in DevOps for automation:
# - Running git commands
# - Running docker commands
# - Running kubectl commands
# - Running Linux shell commands
# WARNING: os.system() is simple but less safe.
# subprocess module is better for complex automation.