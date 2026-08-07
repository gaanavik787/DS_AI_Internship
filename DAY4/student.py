def result():
    total = 0

    for i in range(5):
        marks = int(input("Enter marks: "))
        total = total + marks

    print("Total Marks =", total)

    if total >= 175:
        print("Result = PASS")
    else:
        print("Result = FAIL")

result()