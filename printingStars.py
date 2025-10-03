n=1
while n<=5:
     print ("*"*n)
     n=n+1

total=0

while True:
  users_input= int(input("enter a number (-1 to quit):"))
 print("User typed", users_input)

   print("total is now", total)
   if users_input ==-1:
    break
   total= total + users_input
   print ("total:",total)
print("total",total)