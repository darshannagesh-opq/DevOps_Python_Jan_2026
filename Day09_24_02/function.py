# -----------------------------
# FUNCTIONS — classroom notes
# -----------------------------
# A function is a reusable piece of code that performs a specific task.
# Benefits: code reuse, cleaner code, easier debugging.

# ------------------------------------------------------------------
# 1. Basic function: define and call
# ------------------------------------------------------------------
def greet():
    """A simple function that prints a greeting."""
    print("Hello")

# Call the function multiple times (reuse)
greet()
greet()

# Expected output:
# Hello
# Hello

# ------------------------------------------------------------------
# 2. Functions with parameters (inputs)
# ------------------------------------------------------------------
def greet_name(name):
    """Function with a parameter to greet by name."""
    print("Hello", name)

greet_name("Darshan")
greet_name("Sam")
greet_name("Ravi")

# Expected output:
# Hello Darshan
# Hello Sam
# Hello Ravi

# ------------------------------------------------------------------
# 3. Functions that print vs. functions that return values
# ------------------------------------------------------------------
def add_print(a, b):
    """Prints the sum (has side-effect) — cannot reuse the value easily."""
    print(a + b)

def add_ret(a, b):
    """Returns the sum — caller can reuse the result."""
    return a + b

add_print(3, 4)                # prints 7
output = add_ret(3, 4)         # output variable receives the returned value
print(output)                  # prints 7
print(output * 3)              # prints 21

# Key idea: use return when you need to use the result (composability).

# ------------------------------------------------------------------
# 4. Default parameters
# ------------------------------------------------------------------
def greet_default(name="OPQ"):
    """Parameter with a default value. If caller omits 'name', default is used."""
    print("Hello", name)

greet_default()                # uses default -> Hello OPQ
greet_default("Darshan")       # Hello Darshan
greet_default(name="Darshan")  # named argument, same effect

# ------------------------------------------------------------------
# 5. Keyword arguments (named) and positional arguments
# ------------------------------------------------------------------
def greet_2(name1, name2):
    """Both parameters can be passed by name (keyword) or positionally."""
    print(name1, name2)

# Calling with keyword arguments:
greet_2(name1="sam", name2="ravi")  # prints: sam ravi

# Or positional:
greet_2("sam", "ravi")              # prints: sam ravi

# ------------------------------------------------------------------
# 6. Positional-only and keyword-only parameters (Python 3.8+)
#    Syntax:
#      def func(pos_only1, pos_only2, /, normal, *, kw_only):
#        ...
#    - Parameters before '/' are positional-only.
#    - Parameters after '*' are keyword-only.
# ------------------------------------------------------------------
def exp(a, b, c, d):
    """Simple function that accepts all parameters normally."""
    return a + b + c + d

print(exp(1, 2, 5, 8))  # all positional -> 16

# Example with positional-only and keyword-only:
def exp1(a, b, /, c, *, d):
    """
    a, b  -> positional-only
    c     -> positional or keyword
    d     -> keyword-only (must be passed as d=...)
    """
    return a + b + c + d

# Valid calls:
print(exp1(1, 2, 5, d=8))     # a=1,b=2,c=5,d=8  -> 16
print(exp1(1, 2, c=4, d=8))   # a=1,b=2,c=4,d=8  -> 15
# Invalid: exp1(a=1, b=2, c=4, d=8)  # error: a,b are positional-only

# ------------------------------------------------------------------
# 7. Returning multiple values (tuples) and unpacking
# ------------------------------------------------------------------
def arth(a, b):
    """Return sum, difference and product as a tuple."""
    return a + b, a - b, a * b

print(arth(5, 2))        # prints a tuple (7, 3, 10)

s, d, m = arth(4, 6)     # unpacking into separate variables
print(s, d, m)           # prints: 10 -2 24

# ------------------------------------------------------------------
# 8. Local vs global variables (scope)
# ------------------------------------------------------------------
g = 10  # global variable

def scope_demo():
    """Demonstrates local and global access for read-only usage."""
    l = 5  # local variable
    print("Inside function, local l =", l)
    print("Inside function, global g =", g)

scope_demo()
# print(l)  # ERROR if uncommented: NameError: name 'l' not defined
print("Outside function, global g =", g)

# Example: local variable shadowing a global variable
a = 10

def scope_shadow():
    a = 5  # this 'a' is local to function, does NOT modify global a
    print("Inside:", a)

scope_shadow()
print("Outside:", a)  # prints 10 (unchanged)

# If you need to modify a global variable inside a function, use the 'global' keyword (use sparingly).
a = 10
def scope_modify_global():
    global a
    a = 5   # modifies the global 'a'
    print("Inside (modified):", a)

scope_modify_global()
print("Outside (after modification):", a)  # prints 5

# Better pattern: return new value and reassign in caller (avoids globals).

# ------------------------------------------------------------------
# 9. Returning a local value
# ------------------------------------------------------------------
g = 10
def scope_return_local():
    l = 5
    return l

res = scope_return_local()
print("Returned local value:", res)  # 5

# ------------------------------------------------------------------
# 10. Variable positional arguments (*args) and variable keyword arguments (**kwargs)
#     - *args collects extra positional args as a tuple
#     - **kwargs collects extra keyword args as a dict
# ------------------------------------------------------------------
def many_args(a, b, c, *args):
    """Extra positional arguments are packed into 'args' tuple."""
    print("a, b, c:", a, b, c)
    print("*args:", args)

many_args(1, 2, 3, 4, 5)
# Output:
# a, b, c: 1 2 3
# *args: (4, 5)

def many_args_kwargs(a, b, c, *args, **kwargs):
    """Mix of positional, extra positional and extra keyword args."""
    print("a, b, c:", a, b, c)
    print("*args:", args)
    print("**kwargs:", kwargs)
    print("**kwargs keys:", list(kwargs.keys()))

many_args_kwargs(1, 2, 3, 4, 5, name="rita", age=30)
# Output:
# a, b, c: 1 2 3
# *args: (4, 5)
# **kwargs: {'name': 'rita', 'age': 30}
# **kwargs keys: ['name', 'age']

# Use-case: wrapper functions, forwarding arguments to other functions, flexible APIs.

# ------------------------------------------------------------------
# 11. Type hints (optional, for readability / tooling)
# ------------------------------------------------------------------
def exp_typed(a: int, b: int) -> int:
    """Type hints indicate expected types; not enforced at runtime."""
    return a + b

print(exp_typed(2, 3))
print(exp_typed(2, "abc"))  # runtime will run and produce '2abc' only if + supports it; type hints don't stop it.

# Note: type hints are checked by external tools (mypy, linters) not the interpreter.

# ------------------------------------------------------------------
# 12. Nested functions and composition
# ------------------------------------------------------------------
def multi(a, b):
    """Helper function used inside another function."""
    return a * b

def area_of_rect(length, width):
    """Calls another function to compute area."""
    return multi(length, width)

print("Area of rectangle 2x3 =", area_of_rect(2, 3))