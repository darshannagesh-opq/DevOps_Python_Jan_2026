"""
Python - subprocess Module
Topic:
1. Running system commands
2. Capturing output
3. Checking return codes
4. Command chaining
"""

# =====================================================
# WHAT IS subprocess?
# =====================================================

# subprocess allows Python to run
# system/terminal commands.

# Anything you type in:
# - Command Prompt (Windows)
# - Terminal (Mac/Linux)
# Can be executed using subprocess.


# =====================================================
# BASIC COMMAND EXECUTION
# =====================================================

import subprocess

# Run simple command
subprocess.run("echo Hello from Python!", shell=True)

# shell=True → allows running command as if typed in terminal

# Run directory listing
# subprocess.run("dir", shell=True)

# Create folder
# subprocess.run("mkdir test_folder", shell=True)


# =====================================================
# LIST STYLE (SAFER WAY)
# =====================================================

# Instead of shell=True, we can pass list

subprocess.run(["echo", "Hello from Python!"])

# Recommended when possible for security reasons.


# =====================================================
# CAPTURING OUTPUT
# =====================================================

result = subprocess.run(
    "echo Hello Student",
    shell=True,
    text=True,
    capture_output=True
)

print("Output:", result.stdout)

# text=True → output as string (not bytes)
# capture_output=True → captures stdout & stderr


# =====================================================
# HANDLING ERRORS
# =====================================================

result = subprocess.run(
    "invalidcommand",
    shell=True,
    text=True,
    capture_output=True
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)


# =====================================================
# RETURN CODE
# =====================================================

# returncode = 0 → Success
# returncode != 0 → Error

res = subprocess.run("ping google.com", shell=True)
print("Return code:", res.returncode)


# =====================================================
# COMMAND CHAINING
# =====================================================

# && → Run next command only if previous succeeds
# |  → Pipe output of one command into another

subprocess.run("echo Hello && echo World", shell=True)


# =====================================================
# MULTI-STEP COMMAND EXAMPLE
# =====================================================

cmd = (
    "echo Starting process.. && "
    "mkdir mydata && "
    "cd mydata && "
    "echo This is inside the folder > info.txt && "
    "dir"
)

subprocess.run(cmd, shell=True)


# What happens step-by-step:
# 1. Prints Starting process..
# 2. Creates folder mydata
# 3. Goes inside folder
# 4. Creates file info.txt
# 5. Lists directory contents


# =====================================================
# IMPORTANT SECURITY NOTE
# =====================================================

# Avoid using shell=True with user input.
# It can cause command injection.

# Prefer:
# subprocess.run(["command", "arg1", "arg2"])


# =====================================================
# IMPORTANT POINTS 
# =====================================================

# 1. subprocess runs system commands.
# 2. shell=True allows full shell execution.
# 3. capture_output=True captures result.
# 4. returncode tells success or failure.
# 5. Avoid shell=True with user input (security risk).