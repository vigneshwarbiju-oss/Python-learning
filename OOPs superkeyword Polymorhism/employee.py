class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,dept,name,salary):
        super().__init__(name,salary)
        self.dept=dept

    def display(self):
        print(self.name, self.salary, self.dept)

m1=manager("ECE","Biju", "1000000000")
m1.display()