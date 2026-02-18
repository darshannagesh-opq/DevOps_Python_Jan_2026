"""
Python Basics - Loops
Topic: for loop, range(), nested loops, break, continue, for-else
"""

# =====================================================
# WHY LOOPS?
# =====================================================

# Without loop:
print(1)
print(2)
print(3)
print(4)
print(5)

# Problem:
# Repeating code manually is inefficient.
# Solution: Use loops to repeat automatically.


# =====================================================
# WHAT IS A LOOP?
# =====================================================

# A loop repeats a block of code multiple times.

# Python has two main loops:
# 1. for loop
# 2. while loop

# This file focuses on FOR LOOP.


# =====================================================
# FOR LOOP
# =====================================================

# A for loop runs a block of code
# for each item in a sequence.

# Syntax:
# for variable in sequence:
#     block of code


# =====================================================
# range() FUNCTION
# =====================================================

# range() generates a sequence of numbers.

# range(end) → 0 to end-1

for i in range(5):
    print(i)

# Output:
# 0 1 2 3 4


# range(start, end) → start to end-1

for i in range(1, 6):
    print(i)

# Output:
# 1 2 3 4 5


# range(start, end, step)

# Odd numbers
for i in range(1, 10, 2):
    print(i)

# Even numbers
for i in range(2, 10, 2):
    print(i)


# =====================================================
# MULTIPLICATION TABLE
# =====================================================

n = int(input("Enter a number: "))

for i in range(1, 21):
    print(n, "x", i, "=", n * i)

# Step:
# i starts from 1
# goes until 20
# multiplies each time


# =====================================================
# NESTED LOOPS
# =====================================================

# A loop inside another loop.

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Inner loop runs completely
# for each single iteration of outer loop.


# =====================================================
# DICE PROBABILITY EXAMPLE
# =====================================================

target = 5
count = 0
total = 6 * 6

for i in range(1, 7):
    for j in range(1, 7):
        if i + j == target:
            count += 1

probability = (count / total) * 100
print(f"Pairs: {count}, Probability: {probability:.2f}%")


# =====================================================
# THREE DICE EXAMPLE
# =====================================================

target = 10
count = 0
total = 6 * 6 * 6

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i + j + k == target:
                count += 1

probability = (count / total) * 100
print(f"Triplets: {count}, Probability: {probability:.2f}%")


# =====================================================
# break STATEMENT
# =====================================================

# break stops the loop immediately.

for i in range(1, 11):
    if i == 5:
        print("Stopping at 5")
        break
    print("Number:", i)

# Once break runs → loop ends.


# =====================================================
# continue STATEMENT
# =====================================================

# continue skips current iteration
# and moves to next one.

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Odd:", i)


# =====================================================
# for-else
# =====================================================

# else runs ONLY if loop completes normally
# (no break)

target = 8

for i in range(1, 11):
    if i == target:
        print("Found:", target)
        break
else:
    print("Not found")

# If break executes → else will NOT run.


# =====================================================
# IMPORTANT RULES
# =====================================================

# 1. for loop runs for each item in a sequence.
# 2. range(end) → starts from 0.
# 3. range(start, end) → end is NOT included.
# 4. Nested loops multiply total iterations.
# 5. break stops loop immediately.
# 6. continue skips current iteration.
# 7. for-else runs else only if no break happens.
