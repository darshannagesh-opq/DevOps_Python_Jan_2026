"""
Python OOP - Part 1
Topic:
1. What is OOP?
2. Class and Object
3. Attributes
4. Methods
5. self keyword
"""

# =====================================================
# WHAT IS OOP?
# =====================================================

# OOP → Object Oriented Programming
# It groups data + functions together.

# Instead of writing:
# player1_name
# player1_health
# player2_name
# player2_health

# We group everything into one structure → CLASS


# =====================================================
# CLASS vs OBJECT
# =====================================================

# Class → Blueprint
# Object → Instance of class

# Example:
# Recipe → Blueprint
# Dish → Object created from recipe

# Game example:
# Class Player → name, health, strength
# player1 → object
# player2 → object


# =====================================================
# SIMPLE CLASS WITH ATTRIBUTES
# =====================================================

class Person:
    name = "Default"
    age = 20


# Creating objects
p1 = Person()

print("Object p1:", p1)
print("p1 name:", p1.name)
print("p1 age:", p1.age)

# Modifying object values
p1.name = "Sam"
p1.age = 25

print("After change:", p1.name, p1.age)

# New object
p2 = Person()
print("p2 name:", p2.name)
print("p2 age:", p2.age)

# Note:
# Changing p1 does NOT affect p2.


# =====================================================
# CLASS WITH METHODS
# =====================================================

class Mathematics:

    def greet(self):
        print("Hello World")


math = Mathematics()
math.greet()

# IMPORTANT:
# math.greet() internally becomes:
# Mathematics.greet(math)

# self refers to the object calling the method.


# =====================================================
# REAL EXAMPLE - MATHEMATICS CLASS
# =====================================================

class Mathematics:

    # Factorial method
    def factorial(self, n):
        # Example: 5 → 1*2*3*4*5
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    # Product of list elements
    def list_prod(self, lst):
        product = 1
        for x in lst:
            product *= x
        return product

    # Dot product of two lists
    def dot_product(self, lst1, lst2):

        if len(lst1) != len(lst2):
            raise ValueError("Lists must be same length")

        # Multiply element-wise and sum
        return sum(a * b for a, b in zip(lst1, lst2))


# Creating object
math = Mathematics()

print("Factorial:", math.factorial(5))
print("List product:", math.list_prod([1, 2, 3, 4]))

# [1,2,3] * [4,5,6] → [4,10,18] → sum = 32
print("Dot product:", math.dot_product([1, 2, 3], [4, 5, 6]))


# =====================================================
# IMPORTANT CONCEPTS
# =====================================================

# 1. Class is a blueprint.
# 2. Object is an instance of class.
# 3. self refers to the current object.
# 4. Methods are functions inside class.
# 5. Each object has its own data.
# 6. OOP helps organize large programs.


