s_username = "EMC" 
s_password = "1234"

username = input("Enter user name:")
password = input("Enter user pass:")

def validate():
    if(username == s_username and password == s_password):
        return True
    else:
        return False
a=validate()

print(a)