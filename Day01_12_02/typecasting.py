"""
Python Basics - Type Casting
Topic: Converting one data type to another
"""

# Type Casting means:
# Converting a value from one data type to another.

# Common built-in conversion functions:
# int(), float(), str(), bool()


# -----------------------------------------------------
# Converting to int()
# -----------------------------------------------------

# Float to int (decimal part is removed, NOT rounded)
print(3.14, type(3.14))
print(int(3.14))      # Output: 3
print(int(5.99))      # Output: 5
print(int(-1.12))     # Output: -1

# String to int (must contain only numbers)
a = "123"
print(a, type(a))

b = int(a)
print(b, type(b))

#  Invalid conversion
# print(int("123a"))  # ValueError

# Boolean to int
print(int(True))   # 1
print(int(False))  # 0


# -----------------------------------------------------
#  Converting to float()
# -----------------------------------------------------

# Integer to float
print(float(3))
print(float(0))

# Boolean to float
print(float(True))   # 1.0
print(float(False))  # 0.0

# String to float (must be valid decimal number)
a = "10.5"
print(a, type(a))

b = float(a)
print(b, type(b))

# Invalid conversion
# print(float("abc"))  # ValueError


# -----------------------------------------------------
#  Converting to str()
# -----------------------------------------------------

# int to string
a = 123
print(a, type(a))
print(str(a), type(str(a)))

# float to string
b = 3.14
print(b, type(b))
print(str(b), type(str(b)))

# bool to string
print(str(True), type(str(True)))


# -----------------------------------------------------
# Converting to bool()
# -----------------------------------------------------

# Important Rules:

# Numbers:
# 0 or 0.0  -> False
# Any other number -> True

print(bool(0))          # False
print(bool(0.0))        # False
print(bool(1))          # True
print(bool(0.000001))   # True
print(bool(123))        # True
print(bool(-123))       # True

# Strings:
# Empty string "" -> False
# Any non-empty string -> True

print(bool(""))         # False
print(bool(" "))        # True (space is not empty)
print(bool("0"))        # True
print(bool("False"))    # True

# None also becomes False
print(bool(None))       # False


# -----------------------------------------------------
# Two-Step Conversion
# -----------------------------------------------------

# Example: Convert string decimal to integer

a = "3.14"
print(a, type(a))

b = float(a)      # Step 1: string -> float
print(b, type(b))

c = int(b)        # Step 2: float -> int
print(c, type(c))

# Shortcut
print(int(float(a)))

# Example:
# "3.99" becomes 3 (decimal removed, not rounded)

a = "3.99"
b = str(int(float(a)))
print(b, type(b))


# -----------------------------------------------------
# Extra Important Case
# -----------------------------------------------------

# Spaces inside string numbers are allowed

print(int("     12345 "))  # Output: 12345
