"""
Python OOP - Part 2
Topic:
1. __init__ method (Constructor)
2. Instance variables
3. Object initialization
"""

# =====================================================
# WHAT IS __init__ ?
# =====================================================

# __init__ is a special method (constructor).
# It runs automatically when an object is created.

# It is used to initialize (set up) object data.


# =====================================================
# BASIC __init__ EXAMPLE
# =====================================================

class Person:

    def __init__(self):
        print("Inside __init__: Object created")

    def run(self):
        print("Person is running")


# Creating objects
p1 = Person()
p2 = Person()
p3 = Person()

# Every time object is created,
# __init__ runs automatically.

p1.run()


# =====================================================
# __init__ WITH PARAMETERS
# =====================================================

class Person:

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} is running")


# Creating object with values
p1 = Person("Sam", 25)

print("Name:", p1.name)
print("Age:", p1.age)

p1.run()


# =====================================================
# WHAT IS self?
# =====================================================

# self refers to the current object.

# When we do:
# p1 = Person("Sam", 25)

# Internally:
# Person.__init__(p1, "Sam", 25)

# self = p1
# self.name = "Sam"
# self.age = 25


# =====================================================
# WHY __init__ IS IMPORTANT
# =====================================================

# Without __init__, every object has default values.
# With __init__, we can assign custom values
# during object creation.

# Example:
p2 = Person("Ravi", 30)
print(p2.name, p2.age)


# =====================================================
# KEY DIFFERENCE
# =====================================================

# Class variable → shared by all objects
# Instance variable → belongs to each object

# self.name and self.age are instance variables.


# =====================================================
# IMPORTANT POINTS 
# =====================================================

# 1. __init__ runs automatically when object is created.
# 2. It initializes object data.
# 3. self refers to the current object.
# 4. Instance variables are created using self.
# 5. Each object has its own copy of instance variables.
