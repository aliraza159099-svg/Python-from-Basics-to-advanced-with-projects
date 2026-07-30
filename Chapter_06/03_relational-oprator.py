
'''Retational operator:
  like == >= <= < > are all......

  Logical operator are:
  and or not etc
  '''

age = int(input("Enter your age: "))
status = input("Enter status live or death: ")

#Checking whether anyone is eligible for voting or not
if(age >= 18 and status=="live"):
    print("Eligible for voting")
else:
    print("You are not eleigible for voting ")


