"""
Python OOP - Part 3
Topic:
1. State management
2. Methods modifying object
3. Inheritance
4. dir() inspection
"""

# =====================================================
# AGENT CLASS
# =====================================================

class Agent:

    def __init__(self, name, age, health=None):
        self.name = name
        self.age = age

        # Default health = 100 if not provided
        self.health = 100 if health is None else health

        self.alive = True


    # -------------------------------------------------
    # Display information
    # -------------------------------------------------
    def info(self):
        return f"{self.name}: age={self.age}, health={self.health}, alive={self.alive}"


    # -------------------------------------------------
    # Show current health
    # -------------------------------------------------
    def current_health(self):
        print(f"{self.name}: {self.health}")


    # -------------------------------------------------
    # Reduce health by punch
    # -------------------------------------------------
    def punched(self):
        self.health -= 10

        if self.health < 0:
            self.health = 0


    # -------------------------------------------------
    # Reduce health by shot
    # -------------------------------------------------
    def shot(self):
        self.health -= 50

        if self.health < 0:
            self.health = 0


    # -------------------------------------------------
    # Check if alive
    # -------------------------------------------------
    def is_alive(self):
        self.alive = (self.health > 0)
        return self.alive


# =====================================================
# INHERITANCE
# =====================================================

# Boss inherits from Agent

class Boss(Agent):

    def blow_fire(self):
        print("Blow Fire!")



# =====================================================
# WHAT IS INHERITANCE?
# =====================================================

# class Boss(Agent):
# Means:
# Boss gets ALL properties and methods of Agent.

# Boss has:
# - name
# - age
# - health
# - punched()
# - shot()
# - info()
# - is_alive()
# + its own method blow_fire()


# =====================================================
# DEFAULT ARGUMENT LOGIC
# =====================================================

# health = 100 if health is None else health

# If user does not provide health:
# → health becomes 100

# If user provides custom health:
# → use that value


# =====================================================
# STATE CHANGE CONCEPT
# =====================================================

# Methods like punched() and shot()
# MODIFY the internal state of object.

# This is called:
# Encapsulation of behavior + state.


# =====================================================
# dir() FUNCTION
# =====================================================

print(dir(Agent))

# dir() shows:
# - All methods
# - Built-in attributes
# - Inherited methods


# =====================================================
# IMPORTANT CONCEPTS
# =====================================================

# 1. Objects maintain state.
# 2. Methods modify object state.
# 3. Inheritance allows code reuse.
# 4. Boss IS-A Agent.
# 5. Child class can add new behavior.
# 6. Default parameters help flexible initialization.

