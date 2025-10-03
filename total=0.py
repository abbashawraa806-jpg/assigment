

while True:
   username= str(input("Enter username (admin):"))
   print("username", username)
   
   password= int(input("Enter password (1234):"))
   print("password", password)

   if username=="admin":
     break   
print("Account locked")