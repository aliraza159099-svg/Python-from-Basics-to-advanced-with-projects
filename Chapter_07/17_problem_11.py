'''
****
*  *
*  *
****
'''

'''
num = int(input("Enter your number: "))
num1=num
space=0
end_star=0
for i in range(1,(num+1)):
    print("*"*num1,end="")
    num1=1
    print(" "*space,end="")
    space=num-2
    print("*"*end_star,end="")
    end_star=1
    print("")
print("*"*num)
'''
# Thats can be write as 

num = int(input("Enter your number: "))
for i in range(1,num+1):
    if i == 1 or i == num :
        print("*"*num)
    else:
        print("*",end="")
        print(" "*(num-2),end="")
        print("*",end="")
        print("")

