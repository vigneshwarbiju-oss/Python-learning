class person():
    def __init__(self,name): #here init is constructor, name is parameter
        self.name=name  #set variable name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)#this means parent class, now name biju will come here
        self.grade=grade

    def display(self):
        print(self.name,self.grade)

s1=student("biju","A") # this means object created
s1.display()
