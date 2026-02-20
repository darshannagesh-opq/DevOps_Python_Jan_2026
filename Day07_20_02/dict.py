"""
===========================================================
DICTIONARIES IN PYTHON
===========================================================

A Dictionary is a built-in data type in Python that stores
data in KEY-VALUE pairs.

Syntax:
{
    key1: value1,
    key2: value2,
    ...
}

✔ Keys must be unique
✔ Keys must be immutable (int, string, tuple)
✔ Values can be any data type
✔ Dictionaries are ordered (Python 3.7+)

Difference Between List and Dictionary:

List:
- Uses index
- Ordered
- Access using position
- Not meaningful labels

Dictionary:
- Uses keys
- Labelled / meaningful data
- Access using key name
===========================================================
"""


# ===========================================================
# Creating a Dictionary
# ===========================================================

students = {
    "name": "Sam",
    "age": 25,
    "phone": 122334
}

print("Initial Dictionary:")
print(students)


# Duplicate keys example
d = {1: "Sam", 2: "Robin", 1: "Ravi"}
print("\nDuplicate Key Example:")
print(d)

"""
Note:
If duplicate keys are present,
the last value overwrites previous ones.
"""


# ===========================================================
# Accessing Values
# ===========================================================

print("\nAccessing Values Using Key:")
print(students["name"])

# Using get() method
print("\nUsing get():")
print(students.get("name"))

# If key does not exist
print("\nUsing get() for Missing Key:")
print(students.get("marks"))
print(students.get("marks", "Not Found"))

"""
Difference:
students["marks"] → gives KeyError
students.get("marks") → returns None
students.get("marks", default) → returns default value
"""


# ===========================================================
# Updating Dictionary
# ===========================================================

# Update existing key
students["age"] = 30
print("\nAfter Updating Age:")
print(students)

# Add new key-value pair
students["marks"] = 78
print("\nAfter Adding Marks:")
print(students)

# Update multiple values
students.update({"addr": "Blr", "pincode": "540001"})
print("\nAfter Using update():")
print(students)


# ===========================================================
# Removing Items
# ===========================================================

# pop() → removes key and returns its value
value = students.pop("phone")
print("\nRemoved Phone Value:", value)
print(students)

# pop with default
value = students.pop("marks", "Not Found")
print("\nRemoved Marks Value:", value)
print(students)

# del keyword
del students["age"]
print("\nAfter Deleting Age:")
print(students)

# popitem() → removes last inserted key-value pair
students.popitem()
print("\nAfter popitem():")
print(students)

# clear() → removes all items
students.clear()
print("\nAfter clear():")
print(students)


# ===========================================================
#  Dictionary Methods
# ===========================================================

students = {
    "name": "Sam",
    "age": 25,
    "phone": 122334
}

print("\nDictionary Methods Example:")
print(students)

# keys()
print("\nKeys:")
print(students.keys())

# values()
print("\nValues:")
print(students.values())

# items()
print("\nItems (Key-Value Pairs):")
print(students.items())


# Looping through dictionary

print("\nLooping Through Keys:")
for key in students.keys():
    print(key)

print("\nLooping Through Values:")
for value in students.values():
    print(value)

print("\nLooping Through Key-Value:")
for key, value in students.items():
    print(key, value)


# ===========================================================
# Membership Operator (in)
# ===========================================================

"""
'in' checks only KEYS, not values
"""

print("\nChecking Membership:")
print("age" in students)   # True
print(25 in students)      # False


# ===========================================================
#  Merging Dictionaries
# ===========================================================

a = {"x": 1, "y": 2}
b = {"y": 20, "z": 30}

# Using update()
a.update(b)

print("\nAfter a.update(b):")
print("a =", a)
print("b =", b)

"""
Note:
update() modifies the original dictionary.
If same key exists, value gets overwritten.
"""

# Using unpacking (creates new dictionary)
merge = {**a, **b}

print("\nUsing Dictionary Unpacking:")
print(merge)


# ===========================================================
# Summary
# ===========================================================

"""
✔ Dictionary stores data in key-value pairs
✔ Keys must be unique
✔ Access using key name
✔ get() avoids errors
✔ update() modifies existing dictionary
✔ pop(), del, popitem(), clear() remove elements
✔ keys(), values(), items() used for iteration
✔ 'in' checks only keys
✔ Can merge dictionaries using update() or ** unpacking

End of File
===========================================================
"""