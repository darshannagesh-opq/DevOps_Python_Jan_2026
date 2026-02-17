"""
Python Basics - User Input
Topic: input() function
"""

# =====================================================
# WHAT IS input() ?
# =====================================================

# input() is used to take input from the user.

# IMPORTANT RULE:
# input() ALWAYS returns a STRING.

# Example:

name = input("Enter your name: ")
print(name, type(name))

# Step 1: Program shows message
# Step 2: User types something
# Step 3: input() stores it as STRING


# =====================================================
# Why Type Casting is Needed
# =====================================================

age = input("Enter your age: ")
print(age, type(age))

# Even if user enters 25,
# Python stores it as "25" (string)

# If we try:
# print(age + 5)
# This will give error (string + int not allowed)


# =====================================================
# Converting Input to int
# =====================================================

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

print(x + y)

# Step 1: input() takes value as string
# Step 2: int() converts string to integer
# Step 3: Now mathematical addition happens


# =====================================================
# Converting Input to float
# =====================================================

price = float(input("Enter product price: "))
qty = int(input("Enter quantity: "))

print("Total:", price * qty)

# Example:
# price = 99.5
# qty = 2
# Total = 199.0


# =====================================================
# Common Mistake
# =====================================================

# If we do NOT convert to int:

# a = input("Enter first number: ")
# b = input("Enter second number: ")
# print(a + b)

# If user enters:
# 10 and 20
# Output will be: 1020 (string concatenation)
# NOT 30


# =====================================================
# Shortcut Concept
# =====================================================

# Instead of writing two lines:

# a = input()
# a = int(a)

# We combine them:
# a = int(input())

# This is very common in real programs.


# =====================================================
# KEY POINTS 
# =====================================================

# 1. input() always returns a string.
# 2. Convert using int() or float() when needed.
# 3. Without conversion, + will join strings, not add numbers.
