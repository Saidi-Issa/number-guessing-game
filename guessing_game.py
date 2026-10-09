import random
value=random.randint(1,10)
print("You have three trials to guess the correct value between 1 and 10")
for i in range(1,4):
  uservalue=int(input("Enter the value: "))
  if uservalue== value :
    print("Value is correct")
    break 
  elif uservalue != value:
    print("Value is incorrect")
    print("chose the next value")
    
    print(f"the remaining trial is {3-i}")
   
else:
    print("No more trials left")
    print("The correct value is ",value)
    