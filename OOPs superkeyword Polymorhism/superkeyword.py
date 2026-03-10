class a(): #function
    def __init__(self):#__init__ means constructor
        print("A")

    def display(self):
        print("you are in class A")

class b(): #function
    def __init__(self):#__init__ means constructor
        super().__init__() #superkeyword
        print("B")

    def display(self):
        print("you are in class B")

class c(b,a): #going to use multiple inheritance, it will take 1st left class
    def __init__(self):#__init__ means constructor
        super().__init__() #superkeyword
        print("C")

    def display(self):
        print("you are in class C")

obj1 = c()


