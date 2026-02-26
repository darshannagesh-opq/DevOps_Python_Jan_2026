"""
Python Basics - Exception Handling
Topic: try, except, else, finally, raise
"""

# =====================================================
# WHAT IS AN EXCEPTION?
# =====================================================

# An exception is an event that interrupts
# the normal flow of a program.

# Example:
# Dividing by zero
# Invalid input conversion
# File not found


# =====================================================
# BASIC try - except
# =====================================================

# try block → wrap code that may cause error
# except block → handles the error

try:
    num = int(input("Enter a number: "))
    print("Number:", num)
except ValueError:
    print("Not a valid number")

# If user enters text → ValueError occurs
# Program does NOT crash.


# =====================================================
# HANDLING MULTIPLE EXCEPTIONS
# =====================================================

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ValueError:
    print("Not a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

# First matching except block runs.


# =====================================================
# else BLOCK
# =====================================================

# else runs ONLY if try block has NO error.

try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Not a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)


# =====================================================
# finally BLOCK
# =====================================================

# finally ALWAYS runs
# Used for cleanup (closing files, connections)

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found")

finally:
    print("File closed (cleanup done)")


# =====================================================
# RAISING EXCEPTIONS (raise)
# =====================================================

# We can manually raise an exception.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age:", age)


try:
    age = int(input("Enter age: "))
    check_age(age)

except ValueError as e:
    print("Error:", e)


# =====================================================
# COMBINED EXAMPLE
# =====================================================

try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    ticket_price = 500 / age

except ValueError as e:
    print("Value Error:", e)

except ZeroDivisionError:
    print("Age cannot be zero")

else:
    print("Ticket price:", ticket_price)

finally:
    print("Program finished!")


# =====================================================
# KEY POINTS 
# =====================================================

# 1. try → wrap risky code.
# 2. except → handle errors.
# 3. else → runs if no exception.
# 4. finally → always runs.
# 5. raise → manually create an exception.
# 6. Exception handling prevents program crash.

