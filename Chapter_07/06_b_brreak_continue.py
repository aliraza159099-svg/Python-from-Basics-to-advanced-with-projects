'''
Break Statement break the loop when ts called
'''

ali = True
num = int(input("Enter your number : "))
i = 2
while i < num:
    if(num%i==0):
       ali = False
       break
    
    i = i+1

print(f"The number is prime. "if ali else "The number is not prime." )

'''
Continue skips the particular number or iteration as
'''

for i in range(1,16):
    if i == 10:
        continue #it will not print 10 and keep contiue to print 11 to 15
    print(i)
