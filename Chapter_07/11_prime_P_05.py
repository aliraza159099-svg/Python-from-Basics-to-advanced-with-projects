
# prime number checker
ali = True
num = int(input("Enter your number : "))
i = 2
while i < num:
    if(num%i==0):
       ali = False
       break
    
    i = i+1

print(f"The number is prime. "if ali else "The number is not prime." )


        
        
