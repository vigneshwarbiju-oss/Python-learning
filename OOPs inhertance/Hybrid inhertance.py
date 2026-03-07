#if one class can use another class is called inhertance
# Hybrid inheritance
class dad():#if single, multiple, multilevel, Hierachical are all in same
    def money(self):#is called Hybrid inheritance
        print("dad money")
class land():
    def area(self):
        print("important land")
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
s2=son2()
s2.money()
