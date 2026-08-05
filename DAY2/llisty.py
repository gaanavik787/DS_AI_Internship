stud = [["name","akash"],["age",23],[["marks"],[22,44,55]]]

print("Name:", stud[0][1])
print("Age:", stud[1][1])
print("Marks:", *stud[2][1])