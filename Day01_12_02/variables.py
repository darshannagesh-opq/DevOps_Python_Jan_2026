"""
Python Basics - Variables
Class Topic: Variables (Only)
"""

# -----------------------------------------------------
# Why Do We Need Variables?
# -----------------------------------------------------

# Without variables (hard-coded values)

print(10 + 2)
print(10 - 2)

# Problem:
# If we want to change 10 or 2, we must change it everywhere.
# This is not efficient in real programs.

# With variables (better way)

n = 10
m = 2

print(n + m)
print(n - m)

# Now if we change n or m, it updates everywhere automatically.


# -----------------------------------------------------
# What is a Variable?
# -----------------------------------------------------

# Definition:
# A variable is a container that stores a value in memory.
# It gives a name to a value so we can reuse it.

x = 10
print(x)

# Python automatically understands the type of value.
# (No need to declare int, float, etc.)


# -----------------------------------------------------
# Variable Reassignment
# -----------------------------------------------------

# Variables can change their value.

x = 10
print("Initial value:", x)

x = 20
print("Updated value:", x)

# Python always uses the latest assigned value.


# -----------------------------------------------------
# Multiple Variable Assignment
# -----------------------------------------------------

# Assigning same value to multiple variables

x = y = z = 0
print(x, y, z)

# Assigning different values in one line

a, b, c, d = 1, 3, 5, 6
print(a, b, c, d)


# -----------------------------------------------------
# Swapping Variables
# -----------------------------------------------------

# Python allows swapping without temporary variable.

x = 5
y = 7

print("Before Swapping:", x, y)

x, y = y, x

print("After Swapping:", x, y)


# -----------------------------------------------------
# Variable Naming Rules (Must Follow)
# -----------------------------------------------------

# Rule 1: Must start with a letter or underscore (_)
_a = 5

# Rule 2: Cannot start with a number
# 1a = 10  Invalid

# Rule 3: Can contain letters, digits, underscores
my_variable1 = 100

# Rule 4: Case-sensitive
age = 30
Age = 25
print(age)
print(Age)

# Rule 5: Cannot use Python keywords
# if = 10  Invalid


# -----------------------------------------------------
# Naming Conventions (Best Practice)
# -----------------------------------------------------

# snake_case (Preferred in Python)
full_name = "Darshan"

# camelCase (Not preferred in Python)
fullName = "Darshan"

# PascalCase (Usually used for Classes)

# Professional recommendation:
# Use snake_case for variables.

