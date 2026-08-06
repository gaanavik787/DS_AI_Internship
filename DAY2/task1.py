print("******** Welcome to Shopping ********")


price_list = {
    "apple": 40,
    "banana": 20,
    "mango": 60,
    "orange": 30,
    "grapes": 80,
    "pineapple": 70,
    "watermelon": 90,
    "papaya": 50,
    "guava": 35,
    "strawberry": 100
}

cart = []
total = 0

# Add items to cart
while True:
    item = input("Enter fruit (or type 'done' to finish): ").lower()

    if item == "done":
        break

    price = price_list.get(item, 50)   # Default price = ₹50

    cart.append((item, price))
    total += price

# Display total number of items
print("\nTotal Items:", len(cart))

# Display shopping cart
print("\n---------- Shopping Cart ----------")

for item, price in cart:
    print(item, "- ₹", price)

print("-----------------------------------")
print("Total Cost = ₹", total)

# Convert cart into tuple
cart = tuple(cart)

print("\nCart converted into Tuple:")
print(cart)

# Checkout
while True:
    choice = input("\nType 'exit' to checkout: ").lower()

    if choice == "exit":
        print("\nThank you for shopping!")
        print("Visit Again 😊")
        break
    else:
        print("Invalid input! Please type 'exit' to checkout.")

