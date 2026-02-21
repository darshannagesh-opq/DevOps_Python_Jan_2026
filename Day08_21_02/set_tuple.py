"""
===========================================================
SETS IN PYTHON
===========================================================

A Set is a collection of UNIQUE and UNORDERED elements.

Syntax:
{1, 2, 3}

Important Properties:
✔ Stores only unique values (duplicates removed automatically)
✔ Unordered (no indexing)
✔ Mutable (can add/remove elements)
✔ Cannot contain mutable types like list/dict inside it
===========================================================
"""

# ===========================================================
# Creating a Set
# ===========================================================

my_set = {1, 2, 3, 4, 5}
print(my_set, type(my_set))

"""
If duplicates are given:
{1, 2, 2, 3}
Output → {1, 2, 3}
Duplicates automatically removed
"""


# ===========================================================
# Adding & Removing Elements
# ===========================================================

# add() → Adds a single element
my_set.add(6)
print("After add:", my_set)

# pop() → Removes random element (since set is unordered)
removed = my_set.pop()
print("Removed:", removed)
print("After pop:", my_set)

# discard() → Removes element safely (no error if not found)
my_set.discard(3)
print("After discard:", my_set)

# clear() → Removes all elements
# my_set.clear()


# ===========================================================
# Looping Through a Set
# ===========================================================

for i in my_set:
    print(i)

"""
Note:
Since set is unordered, order may change.
"""


# ===========================================================
# Set Operations
# ===========================================================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

# ---------------- UNION ----------------
# All unique elements from both sets

print("Union using | :", a | b)
print("Union using method:", a.union(b))


# ---------------- INTERSECTION ----------------
# Common elements

print("Intersection using & :", a & b)
print("Intersection using method:", a.intersection(b))


# ---------------- DIFFERENCE ----------------
# Elements in one set but not in other

print("a - b :", a - b)
print("b - a :", b - a)

print("Using method:", a.difference(b))


# ---------------- SYMMETRIC DIFFERENCE ----------------
# Elements in either set but NOT in both

print("Symmetric Difference:", a ^ b)


# ===========================================================
# Removing Duplicates from List Using Set
# ===========================================================

nums = [1, 2, 3, 2, 4, 3, 5, 5, 1, 6, 9]
print("Original List:", nums)

unique_set = set(nums)
print("Unique Set:", unique_set)

unique_list = list(unique_set)
print("Unique List:", unique_list)

"""
Common Use Case:
✔ Remove duplicates
✔ Perform mathematical set operations
"""


# ============================================================
# TUPLES IN PYTHON
# ============================================================

"""
Tuple:
A tuple is similar to a list but IMMUTABLE.

Syntax:
(1, 2, 3)

Properties:
✔ Ordered
✔ Immutable (cannot modify after creation)
✔ Allows duplicate values
✔ Faster than list
✔ Can be used as dictionary keys
============================================================
"""

my_tuple = (1, 2, 4, 5, 6, 7)

print(my_tuple, type(my_tuple))

# Accessing elements
print(my_tuple[0])
print(my_tuple[3])

# Concatenation
t1 = (1, 2)
t2 = (4, 5)
print("Concatenation:", t1 + t2)

# Length
print("Length:", len(my_tuple))

# count()
print("Count of 4:", my_tuple.count(4))

# index()
print("Index of 4:", my_tuple.index(4))

# Repetition
print("Repeat:", my_tuple * 3)


"""
Why Use Tuple?

✔ When data should NOT change
✔ For fixed configuration values
✔ For returning multiple values from functions
✔ As dictionary keys (since immutable)
"""


# ===========================================================
# DIFFERENCE: LIST vs SET vs TUPLE
# ===========================================================

"""
LIST:
✔ Ordered
✔ Allows duplicates
✔ Mutable
✔ Indexed

SET:
✔ Unordered
✔ Unique elements only
✔ Mutable
✔ No indexing

TUPLE:
✔ Ordered
✔ Allows duplicates
✔ Immutable
✔ Indexed
"""

"""
When to Use What?

Use LIST → when order matters & data changes
Use SET → when you need unique elements
Use TUPLE → when data should remain constant
"""

# End of Notes