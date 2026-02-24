# ------------------------------
# main.py  — importing module
# ------------------------------

# Method 1: import entire module
import support

support.greet()
print("20 + 3 =", support.add(20, 3))
print("PI =", support.PI)

# ---------------------------------------------

# Method 2: import only specific functions
from support import add

print(add(2, 3))
# greet()   # ERROR – greet not imported

# ---------------------------------------------

# Method 3: import everything from module (NOT recommended)
from support import *

greet()   # Works because you imported everything

# ---------------------------------------------

# Method 4: Module alias (recommended)
import support as sup

sup.greet()
print(sup.add(5, 6))
print(sup.PI)