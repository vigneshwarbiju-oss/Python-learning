# func without using instance & class variable// def info()
class laptop():
    charger="C-type"
    def __init__(self):
        self.brand=""
        self.price=100
    def setprice(self,price):
        self.price=price
    def getprice(self): #instance method
        print(self.price)#instance method

    @classmethod # @classmethod mean Decorator used for class object not required in call function
    def changecharger(cls):#cls means class method
        cls.charger="B type"
        print("charger changed to B type")

    @staticmethod   # Static method using decorator
    def info():
        print("This is laptop class")

hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changecharger()

hp.info()