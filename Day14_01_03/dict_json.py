"""
Python - JSON Handling
Topic:
1. What is JSON?
2. Writing JSON to file
3. Reading JSON from file
4. Difference between dict and JSON
"""

# =====================================================
# WHAT IS JSON?
# =====================================================

# JSON → JavaScript Object Notation
# Used to store and transfer data.
# Commonly used in:
# - APIs
# - Websites
# - Mobile apps
# - Config files

# JSON looks similar to Python dictionary.


# =====================================================
# WRITING JSON TO FILE
# =====================================================

import json

student = {
    "name": "Rahul",
    "age": 20
}

# json.dump() → write dictionary to JSON file

with open("students.json", "w") as f:
    json.dump(student, f, indent=4)

# indent=4 → makes file readable


# =====================================================
# READING JSON FROM FILE
# =====================================================

with open("students.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))   # dict


# =====================================================
# dict vs JSON
# =====================================================

# Python Dictionary:
# - Exists inside Python program
# - Uses single or double quotes
# - Keys can be any immutable type

# Example:
py_dict = {
    'name': 'Rahul',
    'age': 20
}

# JSON:
# - Text format (string/file format)
# - Used outside Python
# - Keys MUST be double quotes
# - Keys must be strings

# Example JSON format (inside file):
# {
#     "name": "Rahul",
#     "age": 20
# }


# =====================================================
# KEY DIFFERENCES TABLE
# =====================================================

# | Feature         | Python dict         | JSON                     |
# |----------------|--------------------|--------------------------|
# | Exists in      | Python memory       | File / API / Network     |
# | Quotes         | ' or " allowed      | Only double quotes       |
# | Data Types     | Python types        | Limited types            |
# | Boolean        | True / False        | true / false             |
# | Null value     | None                | null                     |


# =====================================================
# IMPORTANT FUNCTIONS
# =====================================================

# json.dump()  → write dict to file
# json.load()  → read JSON file to dict
# json.dumps() → convert dict to JSON string
# json.loads() → convert JSON string to dict


# Example:

json_string = json.dumps(student)
print(json_string)
print(type(json_string))  # str

python_dict = json.loads(json_string)
print(python_dict)
print(type(python_dict))  # dict


# =====================================================
# IMPORTANT POINTS 
# =====================================================

# 1. JSON is a text format.
# 2. Python uses dict internally.
# 3. JSON is used for APIs and data exchange.
# 4. json.load converts JSON → dict.
# 5. json.dump converts dict → JSON.
