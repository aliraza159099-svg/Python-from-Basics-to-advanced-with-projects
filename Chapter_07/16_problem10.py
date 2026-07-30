'''

  *
 ***
*****

'''
num = int(input("enter the number: "))
n=1

for i in range(1,num+1):
        print(" "*(num-i), end="")
        print("*"*n,end="")
        n=n+2
        print("")
