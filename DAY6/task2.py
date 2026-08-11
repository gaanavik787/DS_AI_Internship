import pandas as pd


marks = pd.Series(
    [75, 55, 82, 60, 90],
    index=["Maths", "English", "Python", "Java", "DBMS"]
)

print("Student Marks:")
print(marks)


print("\nMarks at position 0:", marks.iloc[0])
print("Marks at position 2:", marks.iloc[2])


print("\nMaths marks:", marks["Maths"])
print("Python marks:", marks["Python"])


print("\nValues:")
print(marks.values)

print("\nIndex:")
print(marks.index)

print("\nMarks above 60:")
print(marks[marks > 60])