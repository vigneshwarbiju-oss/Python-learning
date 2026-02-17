b = int(input("Enter number:"))
a = []
for i in range(1,b+1):
    a.append(i)
print("First", b, "natural numbers:", a)
print("Sum of the first", b, "natural numbers:", sum(a))

