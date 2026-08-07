import math
import statistics
import time
import datetime
import calendar
import os
import sys
import string


name = input("Enter your name: ")
marks = [80, 75, 90, 85, 70]

print("\nName:", name)
print("Marks:", marks)


print("Total:", sum(marks))
print("Maximum:", max(marks))
print("Minimum:", min(marks))
print("Length:", len(marks))
print("Sorted:", sorted(marks))

# Statistics module
print("\nAverage:", statistics.mean(marks))

# Math module
print("Square Root of Total:", math.sqrt(sum(marks)))
print("Factorial of 5:", math.factorial(5))
print("Value of PI:", math.pi)


# Time module
print("Current Time:", time.ctime())

# Datetime module
print("Current Date:", datetime.date.today())

# Calendar module
print("\nCalendar of August 2026")
print(calendar.month(2026, 8))

# OS module
print("Current Directory:", os.getcwd())

# Sys module
print("Python Version:", sys.version)

# String module
print("Alphabets:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)