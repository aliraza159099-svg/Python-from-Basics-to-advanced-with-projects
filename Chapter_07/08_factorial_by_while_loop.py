'''
Ask the user for a positive integer and calculate 
its factorial using a while loop.
'''
num = int(input("Enter your number: "))
i=1
fact = 1
while (i<=num):
    fact = fact*i
    i=i+1

print(f"The factorial of {num} is : {fact}")
    