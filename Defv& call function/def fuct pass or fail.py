def passfail():
    print("Find pass or fail:")
    a=int(input("Enter Mark:"))
    if(a>=35):
        return("pass")
    else:
        return("fail")
print(passfail())