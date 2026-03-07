class phone():
    charger="C-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Chargertype:",self.charger)
phone.charger="B-type"
samsung=phone("samsung","10000")
Apple=phone("Apple", "75000")
Redmi=phone("Redmi", "75000")
samsung.display()
Apple.display()
Redmi.display()