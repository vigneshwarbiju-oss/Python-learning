class vehicle(): #inheritance
    def start(self):#method
        print("vehicle started.")

class car(vehicle):
    def start(self):
        print("Car started")

s1=vehicle()
s1.start()

s1=car()
s1.start()
