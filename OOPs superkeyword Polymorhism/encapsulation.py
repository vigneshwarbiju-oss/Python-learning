class company():
    def __init__(self):
        self.company="google"#normal variable
# we can access private variable only by using methods in clas

c1=company()
c1.company="googogogle"  #remove this line & try
print(c1.company)