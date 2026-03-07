class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add", self.num1+self.num2)
    def sub(self):
        print("sub", self.num1-self.num2)
    def mul(self):
        print("mul", self.num1*self.num2)
    def div(self):
        print("div", self.num1/self.num2)

obj1=calculator(10,2)   
obj1.add()
obj1.sub()
obj1.mul()
obj1.div()

#without constructor
class cal:
    def add(self,a,b):
        print("add",a+b)
    def sub(self,a,b):
        print("sub",a-b)
    def mul(self,a,b):
        print("mul",a*b)
    def div(self,a,b):
        print("div",a/b)  
a=15
b=3         
cal1=cal()
cal1.add(a,b)
cal1.sub(a,b)
cal1.mul(a,b)
cal1.div(a,b)