class fruit:
    def __init__(self):
        self.fruitname="app"
        self.fruitcolor="ree"
    def display(self):
        print("Name:",self.fruitname)
        print("Color:",self.fruitcolor)
f1=fruit()
f2=fruit()
f1.fruitname="Mango"
f1.fruitcolor="yellow"
f2.fruitname="Apple"
f2.fruitcolor="red"

f1.display()
f2.display()