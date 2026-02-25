# ------------------------------
# support.py  — custom module
# ------------------------------

# A module is simply a .py file containing:
#   - functions
#   - variables
#   - classes (later)
#   - test / demo code (optional)

# This allows:
#   ✔ Code organization
#   ✔ Reuse across multiple files
#   ✔ Easier maintenance


# -------- Functions inside module --------
def greet():
    """Simple function inside module"""
    print("Hello")


def add(a, b):
    """Return addition of two numbers."""
    return a + b


# -------- Module-level constant --------
PI = 3.14


# -------------------------------------------------
# __name__ → Special variable in Python
# -------------------------------------------------
# When a file is RUN directly:
#         __name__ = "__main__"
#
# When a file is IMPORTED as a module:
#         __name__ = "support"
#
# Therefore, the below block runs ONLY when
# support.py is run directly (not imported).
# -------------------------------------------------

if __name__ == "__main__":
    # This block is used for demo/testing code
    print("Inside support.py – running as main file")
    print("10 + 20 =", add(10, 20))

# Purpose:
# Prevents unwanted code execution when imported.