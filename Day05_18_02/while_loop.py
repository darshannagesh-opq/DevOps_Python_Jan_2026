"""
Python Basics - While Loop
Topic: while loop, condition-based repetition
"""

# =====================================================
#  WHAT IS A WHILE LOOP?
# =====================================================

# A while loop runs UNTIL the condition becomes False.

# Syntax:
# while condition:
#     block of code
#     iteration step (important)

# If condition is True → loop runs
# If condition becomes False → loop stops


# =====================================================
# BASIC EXAMPLE
# =====================================================

i = 1

while i <= 5:
    print(i)
    i += 1   # Important: updating variable

# Step:
# i = 1 → print 1
# i = 2 → print 2
# i = 3 → print 3
# i = 4 → print 4
# i = 5 → print 5
# i = 6 → condition becomes False → loop stops


# =====================================================
# IMPORTANT RULE
# =====================================================

# Always update the variable inside the loop.
# Otherwise → Infinite Loop (runs forever)

# Example of infinite loop (DO NOT RUN):

# i = 1
# while i <= 5:
#     print(i)
#     # Missing i += 1 → infinite loop


# =====================================================
# SUM UNTIL THRESHOLD
# =====================================================

threshold = int(input("Enter threshold: "))

i = 1
total = 0

while total < threshold:
    total += i
    print(f"After adding {i} → sum = {total}")
    i += 1

# Loop stops when total becomes >= threshold


# =====================================================
# 5️⃣ WHEN TO USE FOR VS WHILE
# =====================================================

# for → when we KNOW how many times to repeat
# while → when we DON'T know how many times


# =====================================================
# COMPARISON TABLE
# =====================================================

# | Feature               | for loop                     | while loop                    |
# |-----------------------|------------------------------|-------------------------------|
# | When to use           | Known repetitions            | Unknown repetitions           |
# | Depends on            | Sequence (range, list, etc.) | Condition (True/False)        |
# | Risk of infinite loop | Low                          | High if not updated properly  |
# | Example               | Print 1–100                  | Ask password until correct    |


# =====================================================
# KEY POINTS
# =====================================================

# 1. while loop runs until condition becomes False.
# 2. Always update the loop variable.
# 3. Be careful of infinite loops.
# 4. Use while when repetition count is unknown.

