# -----------------------------------------
# MATH MODULE
# -----------------------------------------
import math

# ceil() → smallest integer ≥ x (rounds UP)
print(math.ceil(4.2))   # Output: 5
print(math.ceil(4.9))   # Output: 5

# floor() → largest integer ≤ x (rounds DOWN)
print(math.floor(4.2))  # Output: 4
print(math.floor(4.9))  # Output: 4

# sqrt() → square root
print(math.sqrt(16))    # Output: 4.0

# log(x, base) → logarithm
print(math.log(16, 2))  # Output: 4.0 (because 2⁴ = 16)

# Constants
print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045


# -----------------------------------------
# RANDOM MODULE
# -----------------------------------------
import random

# random() → float between 0.0 and 1.0
print(random.random())  

# randint(a, b) → random integer in [a, b]
print(random.randint(1, 10))

# uniform(a, b) → random float between a and b
print(random.uniform(1.0, 10.0))

# shuffle() → randomize order of a list
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)  # Output: shuffled list (e.g., [3, 5, 1, 2, 4])


# String Library

# Provides predefined sets of characters used in text processing.

# Import
import string

# 2.1 Letter Sets
print(string.ascii_letters)     # abc...ABC...
print(string.ascii_lowercase)   # abc...
print(string.ascii_uppercase)   # ABC...

# 2.2 Numbers
print(string.digits)       # '0123456789'
print(string.hexdigits)    # '0123456789abcdefABCDEF'
print(string.octdigits)    # '01234567'

# 2.3 Punctuation
print(string.punctuation)