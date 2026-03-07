class laptop():
    charger="C-type"
    def __init__(self):
        self.brand=""
        self.price=100
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)
    def changecharger(cls):#cls means class method
        cls.charger="B type"
        print("charger changed to B type")
hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changecharger(laptop)