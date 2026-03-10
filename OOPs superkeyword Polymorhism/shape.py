class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self):
        l=10 
        b=20
        print(l*b)

r1=rectangle()
r1.area()#this area return l*b whith inherit


s1=shape()
print(s1.area())#this area return only 0 with out inherit