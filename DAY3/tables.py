# Function to display the multiplication table
def show_table(num):
    print("\nMultiplication Table of", num)
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Main program
number = int(input("Enter an integer: "))
show_table(number)