x = [32, 44, 3, 22]

print("Original List:", x)

num = int(input("Enter a number: "))
x.append(num)

print("Updated List:", x)
print("Minimum:", min(x))
print("Maximum:", max(x))
print("Sum:", sum(x))
print("Average:", sum(x) / len(x))
print("Length:", len(x))

x.sort()
print("Sorted List:", x)