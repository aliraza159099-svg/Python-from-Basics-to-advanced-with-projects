
a = 2
def even_odd(num):
    # print("<<<<<< Welcome to Even Odd Checker >>>>>>>")
    if num%2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")

while a!=0:
    a = int(input("Enter your number: "))
    #Function Calling
    even_odd(a)