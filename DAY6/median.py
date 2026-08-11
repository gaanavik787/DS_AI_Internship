import numpy as np

# Daily sales of 5 days
sales = np.array([10, 20, 30, 40, 50])

print("Sales:", sales)

# Mean
print("Mean:", np.mean(sales))

# Median
print("Median:", np.median(sales))

# Variance
print("Variance:", np.var(sales))

# Standard Deviation
print("Standard Deviation:", np.std(sales))

# Minimum and Maximum
print("Minimum:", np.min(sales))
print("Maximum:", np.max(sales))

# Sum
print("Total:", np.sum(sales))