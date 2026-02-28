"""
Python Advanced Concepts
Topic:
1. Functions as First-Class Objects
2. Decorators
3. Logging
"""

# =====================================================
# FUNCTIONS AS FIRST-CLASS OBJECTS
# =====================================================

# In Python, functions are treated like normal values.
# That means:
# - Store a function in a variable
# - Pass a function to another function
# - Return a function from another function
# - Store functions inside list, tuple, dict


# -----------------------------------------------------
# Store a function in a variable
# -----------------------------------------------------

def greet():
    print("Hello")

say = greet   # No brackets
say()         # Calls greet()


# -----------------------------------------------------
# Pass function to another function
# -----------------------------------------------------

def call_me(func):
    func()

call_me(greet)


# -----------------------------------------------------
# Return a function from another function
# -----------------------------------------------------

def outer():
    def inner():
        print("Inner function executed")
    return inner

func = outer()
func()

# Short version:
outer()()


# -----------------------------------------------------
# Functions inside list
# -----------------------------------------------------

def a():
    print("Function A")

def b():
    print("Function B")

lst = [a, b]

for f in lst:
    f()


# =====================================================
# DECORATORS
# =====================================================

# Decorator → A function that modifies another function.

# Basic Decorator Example

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# -----------------------------------------------------
# Decorator with Arguments
# -----------------------------------------------------

def log_calc(func):
    def wrapper(a, b):
        print("Starting calculation...")
        result = func(a, b)
        return result
    return wrapper


@log_calc
def add(x, y):
    return x + y

print(add(2, 3))


# -----------------------------------------------------
# Decorator Modifying Return Value
# -----------------------------------------------------

def double(func):
    def wrapper():
        result = func()
        return result * 2
    return wrapper


@double
def number():
    return 10

print(number())

"""
Decorator Example - Access Control
"""

# This decorator checks if the user is admin
def check_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
        else:
            func(user)
    return wrapper


@check_admin
def deploy(user):
    print(f"Deploying application for {user}")


# Test cases
deploy("guest")
deploy("admin")

"""
Python - Logging Module (Complete Notes)
Topic:
1. Why logging?
2. Logging levels
3. basicConfig
4. Logging inside functions
5. Logging with exceptions
6. Real automation script example
"""

# =====================================================
# PRINT VS LOGGING
# =====================================================

# print():
# - Simple
# - Temporary debugging
# - No levels
# - Not recommended for production

# logging:
# - Professional way to track events
# - Supports levels
# - Can save logs to file
# - Used in real-world applications


# =====================================================
# LOGGING LEVELS
# =====================================================

# DEBUG     → Detailed info (developer use)
# INFO      → General info
# WARNING   → Something unexpected
# ERROR     → Serious problem
# CRITICAL  → Very serious failure

# Priority order:
# DEBUG < INFO < WARNING < ERROR < CRITICAL


# =====================================================
# BASIC CONFIGURATION
# =====================================================

import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# level=logging.INFO
# → Only INFO and above will be shown

# format explanation:
# %(asctime)s → current time
# %(levelname)s → log level
# %(message)s → log message


# Example logs

logging.info("Program started")
logging.warning("Low disk space")
logging.error("Something went wrong")


# =====================================================
# LOGGING INSIDE FUNCTIONS
# =====================================================

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return a + b

result = add(5, 3)
logging.info(f"Result is {result}")


# =====================================================
# LOGGING WITH EXCEPTION HANDLING
# =====================================================

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    logging.info(f"Result is {result}")

except ValueError:
    logging.error("Invalid number entered")

except ZeroDivisionError:
    logging.error("Attempted division by zero")


# =====================================================
# REAL AUTOMATION SCRIPT EXAMPLE
# =====================================================

def step1():
    logging.info("Step 1 started - Pulling code from git")
    time.sleep(1)
    logging.info("Step 1 completed")


def step2():
    logging.info("Step 2 started - Building docker")
    time.sleep(1)
    raise Exception("Docker build failed")


def step3():
    logging.info("Step 3 started - Deploying to server")
    time.sleep(1)
    logging.info("Step 3 completed")


logging.info("Automation script started")

try:
    step1()
    step2()
    step3()

except Exception as e:
    logging.error(f"Script Failed due to: {e}")

logging.info("Automation script ended")


# =====================================================
# LOGGING TO FILE (Very Important)
# =====================================================

# Uncomment to log into a file instead of console:

# logging.basicConfig(
#     filename="app.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )


# =====================================================
# IMPORTANT  POINTS
# =====================================================

# 1. Logging is better than print in real projects.
# 2. Use levels correctly.
# 3. ERROR logs should be meaningful.
# 4. Combine try-except with logging.
# 5. Logs help in debugging production issues.

