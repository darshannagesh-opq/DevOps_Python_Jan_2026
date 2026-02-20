"""
===========================================================
MULTI-DIMENSIONAL LISTS IN PYTHON
===========================================================

A multi-dimensional list is a list that contains other lists
as its elements.

The most common example is a 2D list (Matrix).

2D List → Rows and Columns
Example: 3 x 3 matrix
"""

# ===========================================================
# Creating Multi-Dimensional Lists
# ===========================================================

# 3 x 3 Matrix (Rectangular List)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 3 rows, 3 columns


# Real-world example: Student Marks Table (3 x 5)
students = [
    [1, "Asha", 85, 66, 70],
    [2, "Ravi", 43, 33, 66],
    [3, "Mani", 25, 36, 60],
]


# Non-Rectangular List (Jagged List)
# Rows have different lengths
non_rect = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]


# ===========================================================
# Accessing Elements
# ===========================================================

"""
Accessing syntax:

Single element:
matrix[row_index][column_index]

Entire row:
matrix[row_index]
"""

print("Entire Matrix:")
print(matrix)

print("\nFirst Row:")
print(matrix[0])

print("\nIndividual Elements from First Row:")
print(matrix[0][0], matrix[0][1], matrix[0][2])

print("\nElement at Row 1, Column 1:")
print(matrix[1][1])

print("\nLast Row:")
print(matrix[2])


# ===========================================================
# Modifying Elements
# ===========================================================

# Modify a single element
matrix[1][2] = 99
print("\nAfter Modifying matrix[1][2] to 99:")
print(matrix)

# Replace entire row
matrix[0] = [98, 55, 12]
print("\nAfter Replacing First Row:")
print(matrix)

# Add new row at end
matrix.append([10, 11, 12])
print("\nAfter Appending New Row:")
print(matrix)

# Insert row at specific index
matrix.insert(1, [100, 101, 102])
print("\nAfter Inserting Row at Index 1:")
print(matrix)


# ===========================================================
# Deleting Elements
# ===========================================================

# Delete entire row
del matrix[2]
print("\nAfter Deleting Row at Index 2:")
print(matrix)

# Delete specific element
del matrix[0][1]
print("\nAfter Deleting Element matrix[0][1]:")
print(matrix)


# Reset matrix for loop examples
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# ===========================================================
# Looping Through 2D List
# ===========================================================

print("\nUsing Index-Based Loop:")

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()


print("\nUsing Direct Row Iteration:")

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# ===========================================================
# Shallow Copy vs Deep Copy
# ===========================================================

"""
Shallow Copy:
Copies outer list only.
Inner lists still reference same memory.

Deep Copy:
Copies everything (outer + inner lists).
Completely independent copy.
"""

a = [[1, 2], [3, 4]]

# -------- Shallow Copy --------
b = a.copy()

b[0][0] = 99

print("\nShallow Copy Example:")
print("Original:", a)
print("Copied:", b)

# Notice original also changed inside


# -------- Deep Copy --------
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 500

print("\nDeep Copy Example:")
print("Original:", a)
print("Copied:", b)

# Original remains unchanged


# ===========================================================
# List Comprehension
# ===========================================================

"""
===========================================================
LIST COMPREHENSION 
===========================================================

List Comprehension:
A short and clean way to create new lists from existing iterables.

Basic Syntax:
[new_item_expression for item in iterable]

With condition:
[new_item_expression for item in iterable if condition]

Think of it as:
"What to add" + "From where" + "Condition (optional)"
===========================================================
"""

lst = [1, 2, 3, 4, 5, 6]


# ===========================================================
# Squares of Numbers
# ===========================================================

# -------- Traditional Way --------
squares = []
for i in lst:
    squares.append(i * i)

print("\nSquares (Traditional Method):")
print(squares)


# -------- List Comprehension --------
print("\nSquares (List Comprehension):")
print([i * i for i in lst])


# ===========================================================
# Even Numbers Between 0–9
# ===========================================================

# -------- Traditional Way --------
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

print("\nEven Numbers (Traditional):")
print(evens)


# -------- List Comprehension --------
print("\nEven Numbers (List Comprehension):")
print([x for x in range(10) if x % 2 == 0])


# ===========================================================
# Squares of Even Numbers (0–9)
# ===========================================================

# -------- Traditional Way --------
sq_even = []
for x in range(10):
    if x % 2 == 0:
        sq_even.append(x * x)

print("\nSquares of Even Numbers (Traditional):")
print(sq_even)


# -------- List Comprehension --------
print("\nSquares of Even Numbers (List Comprehension):")
print([x * x for x in range(10) if x % 2 == 0])


# ===========================================================
# Convert All Strings to Uppercase
# ===========================================================

names = ["asha", "ravi", "mani"]

# -------- Traditional Way --------
upper_names = []
for name in names:
    upper_names.append(name.upper())

print("\nUppercase Names (Traditional):")
print(upper_names)


# -------- List Comprehension --------
print("\nUppercase Names (List Comprehension):")
print([name.upper() for name in names])


# ===========================================================
# 5️Numbers Greater Than 3
# ===========================================================

# -------- Traditional Way --------
greater_than_3 = []
for num in lst:
    if num > 3:
        greater_than_3.append(num)

print("\nNumbers Greater Than 3 (Traditional):")
print(greater_than_3)


# -------- List Comprehension --------
print("\nNumbers Greater Than 3 (List Comprehension):")
print([num for num in lst if num > 3])


# ===========================================================
# SIMPLE PRACTICE QUESTIONS
# ===========================================================

"""
Practice 1:
Create a list of cubes (x^3) from numbers 1 to 5
→ Do it using:
   1. Traditional loop
   2. List comprehension

Practice 2:
Create a list of only odd numbers from 1 to 20
→ Traditional + List comprehension

Practice 3:
Given:
words = ["apple", "bat", "cat", "elephant"]

Create a new list containing:
- Only words with length > 3
→ Traditional + List comprehension

Practice 4:
Given:
nums = [10, 15, 20, 25, 30]

Create a list where:
- If number is even → multiply by 2
- If number is odd → keep it same
(Hint: Use if-else inside list comprehension)

Practice 5:
Create a list of squares for numbers 1–10
BUT only include squares greater than 20.
"""


# ===========================================================
# BONUS – IF-ELSE INSIDE LIST COMPREHENSION
# ===========================================================

nums = [10, 15, 20, 25, 30]

# Traditional way
result = []
for n in nums:
    if n % 2 == 0:
        result.append(n * 2)
    else:
        result.append(n)

print("\nEven Doubled, Odd Same (Traditional):")
print(result)


# List comprehension with if-else
print("\nEven Doubled, Odd Same (List Comprehension):")
print([n * 2 if n % 2 == 0 else n for n in nums])


"""
Key Rule:
if-else expression comes BEFORE the for loop

Correct:
[value_if_true if condition else value_if_false for item in iterable]
"""


# ===========================================================
#  Summary
# ===========================================================

"""
✔ Multi-dimensional list = list inside list
✔ 2D list behaves like a matrix (rows & columns)
✔ Access using matrix[row][column]
✔ Can modify, append, insert, delete rows or elements
✔ Shallow copy shares inner lists
✔ Deep copy creates fully independent copy
✔ List comprehension makes code shorter and cleaner

End of File
===========================================================
"""