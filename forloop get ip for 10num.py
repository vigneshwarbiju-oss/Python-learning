a=[]
print("Enter 5 numbers:")
for i in range(5):
    num=int(input (f"Enter number {i+1}: "))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print("The sum of the numbers is:",sum)