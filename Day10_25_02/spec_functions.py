"""
Python Basics - Lambda, map(), filter(), zip()
Topic: Functional Programming Tools
"""

# =====================================================
# LAMBDA FUNCTION
# =====================================================

# Lambda is a small, temporary, one-line function.

# Syntax:
# lambda arguments: expression

# It returns the result of the expression automatically.


# -----------------------------------------------------
# Example 1: Square of a number
# -----------------------------------------------------

sq = lambda x: x * x
print(sq(5))  # 25


# -----------------------------------------------------
# Example 2: Add two numbers
# -----------------------------------------------------

add = lambda a, b: a + b
print(add(2, 3))  # 5


# -----------------------------------------------------
# Example 3: Even or Odd
# -----------------------------------------------------

result = lambda x: "Even" if x % 2 == 0 else "Odd"
print(result(3))
print(result(6))

# Direct call without storing:
print((lambda x: "Even" if x % 2 == 0 else "Odd")(11))


# =====================================================
# map() FUNCTION
# =====================================================

# map() applies a function to every element in an iterable.

# Syntax:
# map(function, iterable)

# It returns a map object → convert to list/tuple to see result.


# -----------------------------------------------------
# Example 1: Square each number
# -----------------------------------------------------

nums = [1, 2, 3, 4, 5]

res = map(lambda x: x * x, nums)
print(list(res))


# -----------------------------------------------------
# Example 2: Convert names to uppercase
# -----------------------------------------------------

names = ["sam", "ravi", "robin"]

upper_names = map(lambda n: n.upper(), names)
print(list(upper_names))


# -----------------------------------------------------
# Example 3: Multiply elements of two lists
# -----------------------------------------------------

a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x * y, a, b)
print(list(result))


# =====================================================
# filter() FUNCTION
# =====================================================

# filter() keeps only elements that satisfy a condition.

# Syntax:
# filter(function_returning_True/False, iterable)


# -----------------------------------------------------
# Example 1: Filter even numbers
# -----------------------------------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8]

evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))


# -----------------------------------------------------
# Example 2: Keep marks greater than 50
# -----------------------------------------------------

marks = [25, 45, 67, 88, 90, 34]

high_scores = filter(lambda m: m > 50, marks)
print(list(high_scores))


# =====================================================
# zip() FUNCTION
# =====================================================

# zip() combines multiple iterables element-wise.
# It pairs elements based on index.

# Syntax:
# zip(iterable1, iterable2, ...)


# -----------------------------------------------------
# Example 1: Combine roll numbers and names
# -----------------------------------------------------

roll_nums = ["ABC01", "ABC02", "ABC03"]
names = ["Sam", "Priya", "Arun"]

combined = zip(roll_nums, names)
print(list(combined))

# Convert to dictionary
print(dict(zip(roll_nums, names)))


# -----------------------------------------------------
# Example 2: Combine three lists
# -----------------------------------------------------

cities = ["Delhi", "Blore", "Hyd"]

combined_3 = zip(roll_nums, names, cities)
print(list(combined_3))


# =====================================================
# IMPORTANT RULES
# =====================================================

# 1. Lambda is a small one-line anonymous function.
# 2. map() applies function to every element.
# 3. filter() keeps elements where condition is True.
# 4. zip() combines elements index-wise.
# 5. map(), filter(), zip() return iterators → convert to list() to see result.
