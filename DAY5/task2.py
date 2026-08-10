import numpy as np

# Prices of products in the cart
prices = np.array([120, 275, 95, 180, 325])

increase = 25


updated_prices = prices + increase

print("Original Prices:", prices)
print("Updated Prices:", updated_prices)



prices = [120, 275, 95, 180, 325]

increase = 25

updated_prices = []

for price in prices:
    new_price = price + increase
    updated_prices.append(new_price)

print("Original Prices:", prices)
print("Updated Prices:", updated_prices)