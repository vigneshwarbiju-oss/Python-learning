# we can encapsulation method

class company():
    def __init__(self):
        self.__companyname="google"#if mention "__"is access modifier it will become private variable

# we can access private variable only by using methods in class
    def companyname(self):
        print(self.__companyname)

c1=company()
c1.companyname()