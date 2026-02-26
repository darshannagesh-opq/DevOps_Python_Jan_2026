# programming_practice
# =========================================
# 1. Question Reverse a string without using [::-1] (Without Slicing).

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("devops"))

# Explanation

# We start with an empty string.
# For every character:
# Instead of adding at the end,
# We add it to the front.
# This keeps pushing old characters to the right.

# d → "d"
# e → "ed"
# v → "ved"
# o → "oved"
# p → "poved"
# s → "spoved"

# Concept tested: Loop + string manipulation.

# ============================================

# 2. Count Vowels in a string (case insensitive, ignore spaces).

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    
    for char in s.lower():
        if char in vowels:
            count += 1
    
    return count

print(count_vowels("DevOps Engineer"))

# Explanation

# Convert to lowercase to avoid checking A/E/I/O/U separately.
# Loop through each character.
# Check if character exists in "aeiou".
# Increase counter.

# Concept tested: Loop + membership check (in).

# ============================================

# 3. Check if a string is a palindrome.

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
	
# Convert to lowercase.
# Remove spaces.
# Reverse the string.
# Compare original and reversed.

# =========================================

# 4. FizzBuzz

# Print numbers 1–50:

# Multiple of 3 → Fizz
# Multiple of 5 → Buzz
# Both → FizzBuzz

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
		
# % checks remainder.

# Important: Check both first.
# If you check 3 first, 15 will never reach FizzBuzz.

# Concept tested: Logical operators + condition order.

# =========================================

# 5. Log File Counter - Count occurrences of log types.

logs = ["ERROR", "INFO", "ERROR", "WARNING", "INFO", "ERROR"]

log_count = {}

for log in logs:
    if log in log_count:
        log_count[log] += 1
    else:
        log_count[log] = 1

print(log_count)

# Explanation

# Dictionary used as counter:
# Key → log type
# Value → frequency

# Real DevOps use case:
# Monitoring logs
# Alert thresholds


# =======================================

# 6. Duplicate IPs - Find duplicate IP addresses.

ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3"]

seen = set()
duplicates = set()

for ip in ips:
    if ip in seen:
        duplicates.add(ip)
    else:
        seen.add(ip)

print(list(duplicates))

# Explanation
# Set stores unique values.
# If already seen → it's duplicate.
# Sets automatically avoid repetition.

# Concept tested: Set logic.

# =========================================
# practice questions
# 1. Count Even and Odd Numbers
# 2. Find Maximum Number (Without max())
# 3. Sum of All Values in Dictionary
#     data = {"a": 10, "b": 20, "c": 30}
# 4. Print Only Unique Elements (Without set())
# 5. Find Largest Word in Sentence
#     Find Largest Word in Sentence