class company():
    def __init__(self):
        self._company="google"#normal variable
# we can access private variable only by using methods in clas
class b(company):
    pass
b1=b()
#c1.company="googogogle"  #remove this line & try
print(b1._company)

#single _ means protected variable
#double __ means private variable
#"pass" means public