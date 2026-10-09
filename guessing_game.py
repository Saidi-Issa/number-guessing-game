import random

choose=int(input("Enter 1 for a beginner level, enter 2 for the intermidiate level, enter 3 for the harder level: "))
if choose==1:
    value=random.randint(1,10)
elif choose==2:
    value=random.randint(1,20)
elif choose==3:
    value=random.randint(1,50)
print("You have three trials to guess the correct value between 1 and 10 for beginner level, between 1 and 20 for intermediate level, and between 1 and 50 for harder level")
for i in range(1,4):
  uservalue=int(input("Enter the value: "))
  if uservalue== value :
    print("Value is correct")
    break 
  elif uservalue != value:
       if uservalue>value:
         print("Value is greater than the correct value")
       elif uservalue<value:
         print("Value is less than the correct value")
    print("Value is incorrect")
    print("chose the next value")
    
    print(f"the remaining trial is {3-i}")
   
else:
    print("No more trials left")
    print("The correct value is ",value)
  
