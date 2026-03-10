class animal(): #base class or parent class
    def sound(self): # sound is function
        print("animal makes sound")
#animal class ah dog class inherit pannuthu, so dog class can take animal class sound function
class dog(animal): #another class dog #inheritance from animal class
    def sound(self): 

        print("dog bark")

a1=animal()
a1.sound()
#this is method overriding also called polymorphism









#animal class ah dog class inherit pannuthu, so dog class can take animal class sound function

class animal(): #base class or parent class
    def sound(self): # sound is function
        print("animal makes sound")

class dog(animal): #another class dog #inheritance from animal class
    pass #

a1=dog()
a1.sound()








#animal class ah dog class inherit pannuthu, so dog class can take animal class sound function
class animal(): #base class or parent class
    def sound(self): # sound is function
        print("animal makes sound")
#animal class ah dog class inherit pannuthu, so dog class can take animal class sound function
class dog(animal): #another class dog #inheritance from animal class
    def sound(self): 

        print("dog bark")
class bird(animal): #another class bird #inheritance from animal class
    def sound(self): 
        print("bird sing")
b1=bird()
b1.sound()

