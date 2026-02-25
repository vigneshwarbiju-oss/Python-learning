class laptop:
    def __init__(self):
        self.ram = ""
        self.processor = ""
    def display(self):
        print("Ram:", self.ram)
        print("Processor:", self.processor)
hp=laptop()
dell=laptop()
hp.ram="8GB"
hp.processor="i5"
dell.ram="16GB"
dell.processor="i7"

print(hp.processor)
print(hp.ram)

hp.display()
dell.display()