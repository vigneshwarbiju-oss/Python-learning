class goa:
    name = ""
    drink = ""
    def party(self):
        print("enjoy party")
    def beach(self):
        print("enjoy beach")
        
ramesh = goa()
suresh = goa()

ramesh.name = "Ramesh"
suresh.name = "suresh"

ramesh.drink = "Yes, he drinks"
suresh.drink = "No, didn't"

print(ramesh.name)
print(ramesh.drink)
print(suresh.name)
print(suresh.drink)

ramesh.party()
suresh.beach()