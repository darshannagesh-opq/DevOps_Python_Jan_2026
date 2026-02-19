"""
Python Basics - Data Structures (Lists)
Topic: list - ordered, mutable collection
"""

# =====================================================
# WHAT IS A DATA STRUCTURE?
# =====================================================

# DS (Data Structure) → organizing, storing and managing data.

# Problem without DS:

emp_name1 = "Sam"
emp_phone1 = "788758"
emp_id1 = "ABC123"
emp_DOB1 = "12-12-1980"

# Imagine emp_name2, emp_name3 ...
# Not scalable.
# Hard to read.
# Hard to maintain.


# =====================================================
# BUILT-IN DATA STRUCTURES
# =====================================================

# list
# dict
# set
# tuple

# This file focuses on LIST.


# =====================================================
# WHAT IS A LIST?
# =====================================================

# List is:
# 1. Ordered → keeps insertion order
# 2. Mutable → can change values
# 3. Collection → stores multiple items

# Created using []


# =====================================================
# CREATING LISTS
# =====================================================

students = ["Asha", "Ravi", "Sam"]
print(students)

prices = [20, 1.45, 3.65]
print(prices)

mixed = ["Sam", 12345, "ABC123", "12-12-1980", True]
print(mixed)

empty_list = []
print(empty_list)


# =====================================================
# ACCESSING ITEMS (INDEXING)
# =====================================================

students = ["Asha", "Ravi", "Sam"]

print(students[0])   # Asha
print(students[1])   # Ravi
print(students[2])   # Sam
print(students[-1])  # Sam


# =====================================================
# list() CONVERSION
# =====================================================

# list() converts iterable into list.

name = "Hello"
result = list(name)
print(result)
# ['H', 'e', 'l', 'l', 'o']

sentence = "python is fun"
words = sentence.split()
print(words)


# =====================================================
# SLICING [start:end:step] start inclusive, stop exclusive.
# =====================================================

a = [0, 1, 2, 3, 4, 5, 6]

print(a[2:5])     # [2,3,4]
print(a[:3])      # [0,1,2]
print(a[3:])      # [3,4,5,6]
print(a[1:5:2])   # [1,3]
print(a[::2])     # [0,2,4,6]
print(a[::-1])    # reverse list


# =====================================================
# MODIFYING LISTS
# =====================================================

students = ["Asha", "Ravi", "Sam"]

# Update
students[1] = "Ram"
print(students)

# Add - append()
students.append("Kiran")
print(students)

# Add multiple - extend()
students2 = ["Robin", "Arun"]
students.extend(students2)
print(students)

# Insert at position
students.insert(2, "New Value")
print(students)


# =====================================================
# REMOVING ITEMS
# =====================================================

fruits = ['apple', 'banana', 'apple', 'grapes']

fruits.remove('apple')   # removes first occurrence
print(fruits)

print(fruits.pop())      # removes last item
print(fruits)

print(fruits.pop(1))     # removes index 1
print(fruits)

# Remove all occurrences
nums = [2, 3, 2, 4, 2]

while 2 in nums:
    nums.remove(2)

print(nums)

# clear() removes everything
nums.clear()
print(nums)


# =====================================================
# SEARCHING METHODS
# =====================================================

nums = [2, 3, 2, 4, 2]

print(nums.index(4))  # first index
print(nums.count(2))  # number of occurrences


# =====================================================
# SORTING
# =====================================================

marks = [50, 20, 80, 40]

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

# sorted() does NOT modify original
new_marks = sorted(marks)
print(new_marks)
print(marks)


# =====================================================
# REVERSE
# =====================================================

marks.reverse()
print(marks)


# =====================================================
# COPY - Returns a shallow copy of the list.
# =====================================================

a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)


# =====================================================
# BUILT-IN FUNCTIONS
# =====================================================

a = [1, 2, 3]

print(len(a))
print(max(a))
print(min(a))
print(sum(a))


# =====================================================
# in OPERATOR - in checks whether a value exists inside a list.
# =====================================================

fruits = ['apple', 'banana', 'apple', 'grapes']

print("apple" in fruits)
print("orange" in fruits)


# =====================================================
# LOOPING THROUGH LIST
# =====================================================

for item in fruits:
    print(item)

for i in range(len(fruits)):
    print(i, fruits[i])


# =====================================================
# IMPORTANT RULES 
# =====================================================

# 1. List is ordered.
# 2. List is mutable.
# 3. Index starts from 0.
# 4. Slicing excludes end index.
# 5. sort() changes original list.
# 6. sorted() returns new list.
# 7. remove() removes first match.
# 8. pop() removes by index.


