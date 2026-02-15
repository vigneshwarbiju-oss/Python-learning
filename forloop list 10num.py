b=[]
print("Enter 5 numbers:")
for i in range(5):
    num=int(input ("Enter number "+ str (i+1)+" :"))
    b.append(num)
print(b)

sum=0
for i in b:
    sum=sum+i
print("The sum of the numbers is:",sum)
