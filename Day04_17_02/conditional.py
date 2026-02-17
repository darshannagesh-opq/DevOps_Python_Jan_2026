"""
Python Basics - Conditional Statements
Topic: if, elif, else (Decision Making System)
"""

# =====================================================
# INDENTATION
# =====================================================

# Indentation means leaving spaces before a line of code.
# In Python, indentation defines a block of code.

# If indentation is wrong → SyntaxError

# Example structure:

# if condition:
#     code to run when condition is TRUE

# The code inside the if block must be indented.


# =====================================================
# SIMPLE if STATEMENT
# =====================================================

num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")
    print("Inside if block")

print("Outside block")

# Step:
# If condition is True → run indented block
# If False → skip block


# =====================================================
# if - else
# =====================================================

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Not positive")

print("Outside block")

# if block runs when condition TRUE
# else block runs when condition FALSE


# =====================================================
# if - elif - else
# =====================================================

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# Python checks from TOP to BOTTOM.
# First TRUE condition executes.
# After that, remaining blocks are skipped.


# =====================================================
#  EVEN OR ODD
# =====================================================

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Step:
# num % 2 gives remainder
# If remainder == 0 → Even
# Else → Odd


# =====================================================
# NESTED IF (if inside if)
# =====================================================

age = int(input("Enter age: "))

if age < 13:
    print("Child")
else:
    if age <= 19:
        print("Teenager")
    else:
        print("Adult")

# Better version using elif:

age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")


# =====================================================
# REAL EXAMPLE - TICKET SYSTEM
# =====================================================

age = int(input("Enter age: "))
member = input("Member (y/n): ")

if age > 18:
    if member == "y":
        print("Ticket price is 20/-")
    else:
        print("Ticket price is 25/-")
else:
    if member == "y":
        print("Ticket price is 12/-")
    else:
        print("Ticket price is 15/-")


# =====================================================
# NESTED GRADING SYSTEM
# =====================================================

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
    if marks >= 75:
        print("Grade A")
    else:
        print("Grade B")
else:
    print("Fail")


# =====================================================
# ONE-LINE IF ELSE (TERNARY OPERATOR)
# =====================================================

# Syntax:
# value_if_true if condition else value_if_false

x = 11

print("Even" if x % 2 == 0 else "Odd")

age = 35

print("Child" if age < 13 else
      "Teenager" if age <= 19 else
      "Adult")


# =====================================================
# IMPORTANT RULES
# =====================================================

# 1. Python uses indentation to define blocks.
# 2. Conditions must end with colon (:)
# 3. Only one block runs in if-elif-else.
# 4. Python checks conditions from top to bottom.
# 5. First TRUE condition executes.


# =====================================================
# Coding Practice
# =====================================================

# Take two numbers from user and print the larger one.

# Take three numbers and print the largest.

# Write a program to check whether a number is even or odd.

# Write a grade system:
# 90+ → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail

# Create a simple calculator using:
# number1
# operator (+, -, *, /)
# number2

# Ask username and password.
# If username is "admin" and password is "1234", print "Login Successful".
# Else print "Invalid Credentials".

# ATM system:
# Balance = 5000
# Ask withdrawal amount.
# If amount ≤ balance, print remaining balance.
# Else print "Insufficient funds".

# Write a program to check whether a year is a leap year.