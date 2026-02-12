"""
Python Basics - Data Types
Topic: 4 Basic Data Types in Python
"""

# -----------------------------------------------------
# INTEGER (int)
# -----------------------------------------------------

# Integer represents whole numbers (no decimal).
# It can be positive, negative, or zero.

a = 10
b = -5
c = 0

print(a, type(a))
print(b, type(b))
print(c, type(c))


# -----------------------------------------------------
# FLOAT (float)
# -----------------------------------------------------

# Float represents decimal numbers.

x = 1.5
y = -3.6
z = 0.5

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Important Difference
print(1, type(1))       # int
print(1.0, type(1.0))   # float


# -----------------------------------------------------
# STRING (str)
# -----------------------------------------------------

# String represents text.
# Must be inside single (' ') or double (" ") quotes.

name1 = "Darshan"
name2 = 'Python'

print(name1, type(name1))
print(name2, type(name2))

# KEY RULES

# "Start and end with the same quote type."
#    If you start with single quote, end with single quote.
#    If you start with double quote, end with double quote.

# Correct examples:
print('Hello')
print("Hello")

# Wrong example:
# print('Hello")   # Mismatched quotes -> SyntaxError


# "If your text contains an apostrophe (like Ashish's),
#     prefer double quotes — or use escape sequences."

# Preferred method (using double quotes)
print("Ashish's Laptop")

# Using escape sequence
print('Ashish\'s Laptop')

# Strings that look like numbers are still strings
print("10", type("10"))
print("10.0", type("10.0"))


# -----------------------------------------------------
# BOOLEAN (bool)
# -----------------------------------------------------

# Boolean has only two values:
# True or False

is_active = True
is_admin = False

print(is_active, type(is_active))
print(is_admin, type(is_admin))

# Important difference:
print(True, type(True))       # bool
print("True", type("True"))   # string


# -----------------------------------------------------
# Dynamic Typing
# -----------------------------------------------------

# Python is dynamically typed.
# No need to declare data type explicitly.

a = 10
print(a, type(a))

a = "Now I am a string"
print(a, type(a))

# Python automatically changes the type
# based on assigned value.


"""
Python Basics - print() Function
Topic: sep and end parameters
"""

# -----------------------------------------------------
# Default Behavior of print()
# -----------------------------------------------------

# By default:
# 1. print() adds a SPACE between multiple items
# 2. print() adds a NEWLINE (\n) at the end

print("A", "B", "C")  
# Output: A B C
# (space between items, newline at end)


# -----------------------------------------------------
# sep Parameter (Separator)
# -----------------------------------------------------

# sep controls what separates multiple items
# Default value: sep=" "

print("A", "B", "C", sep="|")
# Output: A|B|C

print("2026", "02", "12", sep="-")
# Output: 2026-02-12

print("Python", "Java", "C++", sep=" -> ")
# Output: Python -> Java -> C++

# Say out loud:
# "sep controls what separates the items."


# -----------------------------------------------------
# end Parameter
# -----------------------------------------------------

# end controls what is printed at the end of print()
# Default value: end="\n" (newline)

print("Hello")
print("World")
# Output:
# Hello
# World

# Removing newline
print("No newline", end="")
print(" next")
# Output: No newline next

# Custom end
print("Loading", end="...")
# Output: Loading...


# -----------------------------------------------------
# Combined Example
# -----------------------------------------------------

print("A", "B", "C", sep="-", end=" END\n")
# Output: A-B-C END


# -----------------------------------------------------
# KEY SUMMARY 
# -----------------------------------------------------

# By default:
# sep = " "
# end = "\n"

# sep  -> controls what separates items
# end  -> controls what ends the print statement
