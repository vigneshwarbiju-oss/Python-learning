#if one class can use another class is called inhertance
# Multilevel inheritance
class grandpa():
    def phone(self):
        print("grandpa phone")

class dad(grandpa):
    def money(self):
        print("Dad's money")

class son(dad):
    def laptop(self):
        print("son's laptop")
    
ram = son()
ram.laptop()
ram.money()

dad=dad()
dad.phone()
