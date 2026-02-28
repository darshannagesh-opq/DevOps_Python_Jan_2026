"""
Python Advanced Concepts
Topic: Iterators and Generators
"""

# =====================================================
# WHAT IS AN ITERATOR?
# =====================================================

# An iterator is an object that allows you
# to traverse (loop through) a sequence.

# List, tuple, string → all are iterable.

# Iterable → can be looped over.
# Iterator → object that actually produces values one by one.


# =====================================================
# USING iter() AND next()
# =====================================================

nums = [1, 2, 3]

it = iter(nums)   # Convert iterable into iterator

print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3

# print(next(it))  # StopIteration error


# =====================================================
# WHAT IS StopIteration?
# =====================================================

# When no more values are left,
# next() raises StopIteration.


# =====================================================
# HOW FOR LOOP WORKS INTERNALLY
# =====================================================

# This:
for i in [10, 2, 4]:
    print(i)

# Internally works like this:

nums = [10, 2, 4]
it = iter(nums)

while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        break


# =====================================================
# GENERATORS
# =====================================================

# Generator is a special type of iterator.
# It uses 'yield' instead of 'return'.

# yield → pauses the function and returns value.


# -----------------------------------------------------
# Simple Generator Example
# -----------------------------------------------------

def simple_gen():
    yield 1
    yield 2
    yield 3

g = simple_gen()

for value in g:
    print(value)


# =====================================================
# NORMAL FUNCTION VS GENERATOR
# =====================================================

# Normal function returns everything at once.

def normal():
    return [1, 2, 3]

print(normal())


# Generator returns one value at a time.

def count_nums_gen():
    for i in range(1, 6):
        yield i

for i in count_nums_gen():
    print(i)


# =====================================================
# MEMORY DIFFERENCE
# =====================================================

# Normal function:
# - Stores entire list in memory.
# - More memory usage.

# Generator:
# - Generates one value at a time.
# - Memory efficient.
# - Useful for large data.


# =====================================================
# IMPORTANT CONCEPTS
# =====================================================

# 1. iter() converts iterable into iterator.
# 2. next() gets next value.
# 3. StopIteration stops iteration.
# 4. for loop automatically handles StopIteration.
# 5. yield makes a function a generator.
# 6. Generators are memory efficient.


# =====================================================
# END OF ITERATORS & GENERATORS CLASS
# =====================================================