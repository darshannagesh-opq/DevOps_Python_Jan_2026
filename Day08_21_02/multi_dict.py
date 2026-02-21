"""
===========================================================
NESTED DICTIONARIES IN PYTHON
===========================================================

A Nested Dictionary is a dictionary where:
- A key maps to another dictionary
- Or contains dictionary + list inside it

It is used to represent structured / hierarchical data.

Example:
Student Database
Each Roll Number → Contains:
    - Basic Details
    - Marks
    - Contact Numbers
===========================================================
"""

# ===========================================================
# Structure of Nested Dictionary
# ===========================================================

students = {
    101: {
        "basic": {"name": "Sam", "age": 17, "class": "12th"},
        "marks": {"math": 67, "english": 41},
        "contacts": ["12345", "54321"]
    },
    102: {
        "basic": {"name": "Robin", "age": 18, "class": "12th"},
        "marks": {"math": 47, "english": 81},
        "contacts": ["331", "22334"]
    }
}

"""
Hierarchy:

students
   ├── 101
   │     ├── basic → dict
   │     ├── marks → dict
   │     └── contacts → list
   └── 102
"""


# ===========================================================
# Accessing Nested Data
# ===========================================================

"""
Access pattern:
dict[key1][key2][key3]

Example:
students[101]["basic"]["age"]
"""

print(students[101])                          # Entire student 101
print(students[101]["basic"])                 # Basic details
print(students[101]["basic"]["age"])          # Age
print(students[102]["marks"]["math"])         # Math marks
print(students[102]["contacts"][0])           # First contact


# ===========================================================
# Updating Nested Data
# ===========================================================

# Update name
students[101]["basic"]["name"] = "Ravi"

# Add new student
students[103] = {
    "basic": {"name": "Asha", "age": 17, "class": "12th"},
    "marks": {},
    "contacts": []
}

print(students)


# ===========================================================
# setdefault() in Nested Dictionary
# ===========================================================

"""
setdefault() ensures that a key exists.
If not present, it creates it.

Useful when working with deeply nested dictionaries.
"""

students.setdefault(104, {}).setdefault("marks", {})["math"] = 50

print(students)


# ===========================================================
# Deleting Nested Data
# ===========================================================

# Delete student safely (avoid KeyError)
students.pop(105, None)

# Delete a subject safely
students[102]["marks"].pop("Science", None)

print(students)


# ===========================================================
# Looping Through Nested Dictionary
# ===========================================================

for roll, info in students.items():
    name = info["basic"]["name"]
    math = info["marks"].get("math", "N/A")
    print(f"Roll: {roll} | Name: {name} | Math: {math}")


"""
.items() returns:
(key, value)

Here:
roll → student roll number
info → nested dictionary
"""


# ===========================================================
# Dictionary Comprehension
# ===========================================================

"""
Dictionary Comprehension:
Short way to create dictionaries.

Syntax:
{key_expression : value_expression for item in iterable}

With condition:
{key_expression : value_expression for item in iterable if condition}
"""


# Traditional way
res = {}
for i in range(1, 6):
    res[i] = i * i

print(res)


# Dictionary comprehension
res = {i: i * i for i in range(1, 6)}
print(res)


# Only even numbers
sq = {x: x * x for x in range(1, 11) if x % 2 == 0}
print(sq)


# ===========================================================
# Summary
# ===========================================================

"""
✔ Nested dictionary = dictionary inside dictionary
✔ Used for structured data (students, employees, products)
✔ Access using multiple keys
✔ setdefault() prevents KeyError while inserting
✔ pop(key, None) avoids errors while deleting
✔ items() useful for looping
✔ Dictionary comprehension makes code shorter

===========================================================
"""