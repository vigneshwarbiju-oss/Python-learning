#if one class can use another class is called inhertance
# Hierarchy inheritance
class dad():#Base class - if only one base class are deriving more that 2 or more
    def money(self):#is called Hiearchical inheritance
        print("dad money")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
s2=son2()
s2.money()
