#if one class can use another class is called inhertance
class dad():
    def phone(self):
        print("Dad's phone")

class mom(): #
    def sweet(self):
        print("mom's sweet")

class son(dad,mom):# if only dad Single inheritance - one funtioin to another function
    def laptop(self):# if dad & mom Multiple inheritance - one funtioin to another function
        print("son's laptop")

ram=son()
ram.laptop()
ram.phone()
ram.sweet()