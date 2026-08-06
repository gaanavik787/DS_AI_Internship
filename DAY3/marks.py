def get_student_name():
    """Function to get student name"""
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty! Please try again.")

def get_marks():
    """Function to get marks using while loop and store in list"""
    marks = []  
    mark_number = 1
    
    print("\nEnter marks (type 'done' to finish):")
    print("-" * 35)
    
    while True:
        user_input = input(f"Enter mark {mark_number}: ").strip()
        
        
        if user_input.lower() == 'done':
            if len(marks) == 0:
                print("⚠️  No marks entered! Please enter at least one mark.")
                continue
            break
        
        
        try:
            mark = float(user_input)
            if 0 <= mark <= 100:
                marks.append(mark)  # Storing mark in list
                mark_number += 1
            else:
                print("❌ Invalid! Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input! Please enter a number or 'done'.")
    
    return marks

def calculate_average(marks):
    """Function to calculate average of marks"""
    if not marks:
        return 0
    return sum(marks) / len(marks)

def calculate_grade(percentage):
    """Function to calculate grade based on percentage"""
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def display_summary(name, marks):
    """Function to display the summary"""
    if not marks:
        print("No marks to display!")
        return
    
    
    total = sum(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    num_subjects = len(marks)
    
    
    print("\n" + "="*55)
    print("📊 STUDENT MARKS SUMMARY".center(55))
    print("="*55)
    print(f"👤 Student Name: {name}")
    print(f"📚 Total Subjects: {num_subjects}")
    print("\n📝 Marks Details:")
    print("-" * 55)
    
    
    for index, mark in enumerate(marks, 1):
        print(f"   Subject {index:2d}: {mark:>6.2f}")
    
    print("-" * 55)
    print(f"💰 Total Marks: {total:>8.2f}")
    print(f"📊 Average Marks: {average:>6.2f}")
    print(f"🏆 Grade: {grade:>12s}")
    print("="*55)

def main():
    """Main function to run the program"""
    print("🎓 STUDENT MARKS MANAGEMENT SYSTEM".center(55))
    print("="*55)
    
    while True:
        
        name = get_student_name()
        
        
        marks = get_marks()
        
       
        display_summary(name, marks)
        
        
        print("\n" + "-"*55)
        choice = input("Do you want to enter marks for another student? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\n👋 Thank you for using the system!")
            break
        print("\n" + "="*55 + "\n")

if __name__ == "__main__":
    main()