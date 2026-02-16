a=int(input("Enter input number :"))
print(a)
print("Expected Output:")
b=[]
for i in range(1,a+1):
    b.append(i)
    print("Number is :", i, "and cube of", i,"is:", i*i*i)