def get_number():
    """Function to get a valid integer from user"""
    while True:
        try:
            num = int(input("Enter an integer to see its multiplication table: "))
            return num
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.")

def get_range():
    """Function to get the range for the table"""
    while True:
        try:
            print("\nChoose table range:")
            print("1. Default (1 to 10)")
            print("2. Custom range")
            
            choice = input("Enter your choice (1 or 2): ").strip()
            
            if choice == '1':
                return 1, 10
            elif choice == '2':
                start = int(input("Enter starting number: "))
                end = int(input("Enter ending number: "))
                if start <= end:
                    return start, end
                else:
                    print("❌ Start must be less than or equal to end!")
            else:
                print("❌ Invalid choice! Please enter 1 or 2.")
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")

def generate_table(num, start, end):
    """Function to generate multiplication table"""
    table = []
    for i in range(start, end + 1):
        result = num * i
        table.append((i, result))
    return table

def display_table(num, table, start, end):
    """Function to display the multiplication table"""
    print("\n" + "="*50)
    print(f"📊 MULTIPLICATION TABLE OF {num}".center(50))
    print("="*50)
    print(f"{'Multiplier':<15} {'Operation':<20} {'Result':<15}")
    print("-"*50)
    
    for multiplier, result in table:
        print(f"{multiplier:<15} {num} × {multiplier:<5} = {result:<15}")
    
    print("="*50)
    
    # Additional statistics
    results = [result for _, result in table]
    print(f"\n📈 Statistics for Table of {num}:")
    print(f"   Range: {start} to {end}")
    print(f"   Total entries: {len(table)}")
    print(f"   Smallest result: {min(results)}")
    print(f"   Largest result: {max(results)}")
    print(f"   Sum of results: {sum(results)}")
    print("="*50)

def display_formatted_table(num, start, end):
    """Function to display table in different format"""
    print("\n" + "="*50)
    print(f"📊 {num} TABLE (ALTERNATIVE VIEW)".center(50))
    print("="*50)
    
    # Display in grid format
    for i in range(start, end + 1):
        if i % 5 == 0 and i > start:
            print()  # New line after every 5 entries
        print(f"{num} × {i:2d} = {num*i:3d}", end="  ")
    
    print("\n" + "="*50)

def save_table_to_file(num, table):
    """Function to save table to a file"""
    try:
        filename = f"table_{num}.txt"
        with open(filename, 'w') as file:
            file.write(f"Multiplication Table of {num}\n")
            file.write("="*30 + "\n")
            for multiplier, result in table:
                file.write(f"{num} × {multiplier} = {result}\n")
        print(f"✅ Table saved to '{filename}'")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

def main():
    """Main function to run the multiplication table program"""
    print("🎓 MULTIPLICATION TABLE GENERATOR".center(50))
    print("="*50)
    
    while True:
        # Get the number
        num = get_number()
        
        # Get the range
        start, end = get_range()
        
        # Generate the table
        table = generate_table(num, start, end)
        
        # Display the table
        display_table(num, table, start, end)
        
        # Show alternative view
        display_formatted_table(num, start, end)
        
        # Ask to save
        save_choice = input("\n💾 Save table to file? (yes/no): ").strip().lower()
        if save_choice == 'yes':
            save_table_to_file(num, table)
        
        # Ask to continue
        print("\n" + "-"*50)
        choice = input("Generate another table? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\n👋 Thank you for using the Multiplication Table Generator!")
            break
        print("\n" + "="*50 + "\n")

# Run the program
if __name__ == "__main__":
    main()