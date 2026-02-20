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

ramesh.drink = "Yes"
suresh.drink = "No"

print(ramesh.name)
print(ramesh.drink)
print(suresh.name)
print(suresh.drink)

ramesh.party()
suresh.beach()
