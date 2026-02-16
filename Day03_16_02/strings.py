"""
Python Basics - Strings
Topic: String Creation, Indexing, Slicing, Methods, Formatting
"""

# =====================================================
# WHAT IS A STRING?
# =====================================================

# A string is text inside single ('') or double ("") quotes.

s1 = "Darshan"
print(s1)

# String Concatenation (+)
print("OPQ" + "Tech")          # No space
print("OPQ" + " " + "Tech")    # With space

# String Repetition (*)
print("ha" * 3)  # hahaha


# -----------------------------------------------------
# Multi-line String (Triple Quotes)
# -----------------------------------------------------

s = '''I'm learning
Python String
'''
print(s)

# This will cause error (multi-line inside normal quotes)
# s2 = "I'm learning
# Python String
# "


# =====================================================
# len() FUNCTION
# =====================================================

name = "Opq tech"
print(len(name))  # Counts total characters (including spaces)


# =====================================================
# INDEXING
# =====================================================

# Each character has a position (index)
# Index starts from 0

text = "Python"

#  P  y  t  h  o  n
#  0  1  2  3  4  5

print(text[0])  # P
print(text[1])  # y
print(text[5])  # n

# Negative Indexing (starts from end)

#  P   y   t   h   o   n
# -6  -5  -4  -3  -2  -1

print(text[-1])  # n
print(text[-3])  # h


# =====================================================
# SLICING
# =====================================================

# Syntax: string[start:end]
# start included
# end NOT included

text = "Python"

print(text[0:3])   # Pyt (0,1,2)
print(text[3:])    # from index 3 to end
print(text[:2])    # from start to index 2 (not included)
print(text[:])     # full string


# =====================================================
# CASE METHODS
# =====================================================

name = "opQ tEcH"

print(name.lower())       # all lowercase
print(name.upper())       # all uppercase
print(name.title())       # First letter of each word capital
print(name.capitalize())  # First letter capital only


# =====================================================
# STRIP METHODS
# =====================================================

# Removes unwanted spaces from start and/or end

text = "         Python        "

print(text.strip())   # both sides
print(text.lstrip())  # left only
print(text.rstrip())  # right only


# =====================================================
# REPLACE METHOD
# =====================================================

msg = "hello world"

print(msg.replace("world", "OPQ"))
print(msg)  # Original string not changed (strings are immutable)

print("banana".replace("a", "A"))


# =====================================================
# COUNT METHOD
# =====================================================

text = "abracadabrabr"

print(text.count("a"))
print(text.count("z"))
print(text.count("abr"))


# =====================================================
# FIND vs INDEX
# =====================================================

text = "abracadabrabr"

# find() → returns index, if not found returns -1
print(text.find("abr"))
print(text.find("cad"))
print(text.find("czzzd"))  # -1

# index() → returns index, if not found gives error
print(text.index("abr"))
print(text.index("cad"))

# This will cause error
# print(text.index("czzzd"))


# =====================================================
# STARTSWITH & ENDSWITH
# =====================================================

line = "Hello world"

print(line.startswith("Hel"))
print(line.endswith("ld"))
print(line.endswith("ldsd"))


# =====================================================
# islower(), isupper()
# =====================================================

print("abc".islower())
print("ABC".islower())
print("ABC".isupper())


# =====================================================
# STRING FORMATTING
# =====================================================

name = "OPQ"
age = 5

# Old method (concatenation)
print("Hello " + name + " , age " + str(age))

# f-string (Recommended method)
print(f"Hello {name}, age {age}")


# =====================================================
# IMPORTANT NOTES
# =====================================================

# Strings are IMMUTABLE
# That means once created, they cannot be changed.
# Methods like replace() return a new string.

# Index starts from 0.
# Slicing does NOT include the end index.