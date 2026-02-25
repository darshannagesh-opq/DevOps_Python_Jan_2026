"""
Python Basics - Date & Time
Topic: datetime module
"""

# =====================================================
# IMPORTING DATETIME
# =====================================================

# Method 1
import datetime

print(datetime.datetime.now())     # current date + time
print(datetime.date.today())       # current date only
print(datetime.datetime.now().time())  # current time only


# =====================================================
# CREATING CUSTOM DATE & TIME
# =====================================================

# Creating a specific date
d = datetime.date(2026, 1, 23)
print(d)

# Creating a specific time
t = datetime.time(9, 30, 45)
print(t)


# =====================================================
# USING from datetime import
# =====================================================

# Cleaner way to import specific classes
from datetime import datetime, timedelta

now = datetime.now()
print("Current datetime:", now)


# =====================================================
# ADDING / SUBTRACTING TIME (timedelta)
# =====================================================

future = now + timedelta(days=7, hours=2)
print("Future datetime:", future)

# You can add:
# days
# hours
# minutes
# seconds


# =====================================================
# FORMATTING DATE (strftime)
# =====================================================

# strftime → convert datetime to formatted string

# Common format codes:

# | Code | Meaning       |
# | ---- | ------------- |
# | %Y   | Year (2025)   |
# | %m   | Month (01-12) |
# | %d   | Day           |
# | %H   | Hour (24h)    |
# | %M   | Minutes       |
# | %S   | Seconds       |
# | %A   | Weekday name  |
# | %B   | Month name    |

print(now.strftime("%Y-%B-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A, %B %d"))


# =====================================================
# DATE DIFFERENCE
# =====================================================

d1 = datetime(2026, 1, 1)
d2 = datetime(2026, 1, 25)

diff = d2 - d1

print("Difference in days:", diff.days)

# Result:
# timedelta object is returned
# diff.days gives number of days


# =====================================================
# IMPORTANT RULES
# =====================================================

# 1. datetime.now() gives current date and time.
# 2. date.today() gives current date only.
# 3. timedelta is used for adding or subtracting time.
# 4. strftime formats date into readable string.
# 5. Subtracting two dates gives timedelta.
