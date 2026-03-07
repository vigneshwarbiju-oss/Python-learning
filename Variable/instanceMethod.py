class laptop():
    chargertype="C-type"
    def __init__(self):
        self.brand=""
        self.price=100
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)
hp=laptop()
hp.setprice(20000)
hp.getprice()