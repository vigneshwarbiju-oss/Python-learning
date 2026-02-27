class student:
    def __init__(self):
        self.name="asdf"
        self.regno="12435"
    def display(self):
        print("Name:",self.name)
        print("regno:",self.regno)
s1=student()
s2=student()
s1.name="biju"
s1.regno="1"
s2.name="vignesh"
s2.regno="2"

s1.display()
s2.display()