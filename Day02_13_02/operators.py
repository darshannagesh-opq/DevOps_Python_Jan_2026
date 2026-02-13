"""
Python Basics - Operators
Topic: Arithmetic, Comparison, Logical, Assignment, Precedence
"""

# -----------------------------------------------------
# WHAT ARE OPERATORS?
# -----------------------------------------------------

# Operators are symbols that tell Python to perform
# a specific operation on values (data types).


# =====================================================
# ARITHMETIC OPERATORS
# =====================================================

# Used for mathematical operations

# Addition (+)
print(2 + 2)
print(2 + 3.5)
print(2.5 + 3.5)

# String Concatenation (+)
print("Hello" + "World")
print("OPQ" + "tech")

# Boolean behaves like numbers (True=1, False=0)
print(2 + True)   # 2 + 1 = 3

# Invalid
# print(2 + "3")  # TypeError


# -----------------------------------------------------
# Subtraction (-)
# -----------------------------------------------------

print(5 - 2)
print(5.5 - 3.2)
print(True - False)  # 1 - 0 = 1

# Invalid
# print("Hello" - "World")


# -----------------------------------------------------
# Multiplication (*)
# -----------------------------------------------------

print(2 * 3)
print(2.5 * 3.5)

# Boolean multiplication
print(2 * True)  # 2 * 1 = 2

# String repetition
print("ha" * 3)
print(2 * "Hello")

#  Invalid
# print("ha" * 2.5)


# -----------------------------------------------------
# True Division (/)
# -----------------------------------------------------

# Always returns float
print(4 / 2)
print(7 / 2)


# -----------------------------------------------------
# Floor Division (//)
# -----------------------------------------------------

# Returns only quotient (removes decimal part)
print(7 // 2)
print(4.5 // 2.2)


# -----------------------------------------------------
# Modulo (%)
# -----------------------------------------------------

# Returns remainder
print(7 % 2)
print(5.5 % 2)


# -----------------------------------------------------
# Exponentiation (**)
# -----------------------------------------------------

print(3 ** 2)
print(pow(3, 5))

# Useful built-in functions
print(abs(-35))          # Absolute value
print(round(3.14159, 2)) # Round to 2 decimal places


# =====================================================
# COMPARISON OPERATORS
# =====================================================

# Used to compare values
# Result is always True or False

print(1 == 1)
print(1 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 3)
print(7 <= 5)

# Boolean comparison
print(True > False)  # 1 > 0 → True

# Invalid
# print(1 > "A")


# =====================================================
# LOGICAL OPERATORS
# =====================================================

# and → both conditions must be True
print(True and True)
print(True and False)

# or → at least one condition must be True
print(True or False)
print(False or False)

# not → reverses boolean value
print(not True)
print(not False)


# =====================================================
# OPERATOR PRECEDENCE (ORDER OF EXECUTION)
# =====================================================

# Order:
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. >, <, >=, <=, ==, !=
# 6. not
# 7. and, or

# -----------------------------------------------------
# IMPORTANT RULE: LEFT TO RIGHT
# -----------------------------------------------------

# If operators have SAME precedence,
# Python evaluates them from LEFT to RIGHT.

print(2 + 3 * 4)
# “Multiplication has higher priority than addition.
# So Python does: 3 * 4 = 12, then 2 + 12 = 14.”

print(10 - 2 + 5)
# “When operators have the same priority, Python evaluates left to right.
# 10 - 2 = 8
# 8 + 5 = 13.”

print(5 + 2 * 3 ** 2)
# “Order:
# Exponent → 3 ** 2 = 9
# Multiplication → 2 * 9 = 18
# Addition → 5 + 18 = 23
# Answer is 23.”

print((5 + 2) * 3)
# “Parentheses have highest priority, so:
# (5 + 2) = 7
# 7 * 3 = 21”

print(20 / 5 * 2)

print(10 > 5 and 3 * 2 == 6)
# Steps:
# Multiplication → 3 * 2 = 6
# Comparison → 10 > 5 → True
# Comparison → 6 == 6 → True
# Logical and → True and True → True

print(5 + 3 > 6 or not 2 == 2)
# Addition → 5 + 3 = 8
# Comparison → 8 > 6 → True
# Comparison → 2 == 2 → True
# not True → False
# Now final:
# True or False → True

print(5 > 3 and 10 > 5)       # True and True → True
print(2 == 2 or 2 == 3)       # True or False → True
print(not (10 < 5))           # not False → True
print(7 != 8 and 1 < 2)       # True and True → True

print((5 > 2) and (3 < 1))           # True and False → False

print((10 == 10) or (20 != 20))      # True or False → True

print(not (7 >= 7 and 8 < 3))        # not (True and False)
                                     # not False → True

print((4 != 5) and not (2 == 2))     # True and not True → True and False → False

print((100 > 50) or (20 > 90 and 5 < 1))


# =====================================================
# ASSIGNMENT OPERATORS
# =====================================================

# = basic assignment
n = 10

# += (add and assign)
n += 5   # n = n + 5
print(n)

# -=
n -= 5
print(n)

# *=
n *= 3
print(n)

# /=
n /= 2
print(n)

# //=
n //= 2
print(n)

# %=
n %= 2
print(n)

# **=
n **= 2
print(n)


