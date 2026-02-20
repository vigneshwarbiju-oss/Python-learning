n = int(input("Enter number: "))
a = []
for i in range(1, n+1):
    a.append(i)

print("First", n, "natural numbers:", a)
print("Sum of the first", n, "natural numbers:", sum(a))