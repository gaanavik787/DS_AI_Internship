try:
    # Prompt user for age input and convert it to an integer
    age = int(input("Enter your age: "))
    
    # Validate the age value
    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
        
except ValueError:
    # Handle non-integer inputs (like words or symbols)
    print("Invalid input. Please enter a valid number.")
