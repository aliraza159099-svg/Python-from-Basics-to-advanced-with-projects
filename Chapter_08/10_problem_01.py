'''
Write a program to convert farenhite to Celcius
c = 5 * (f-32)/9
'''

def F_to_C(f):
    return 5 * (f-32)/9

f = int(input("Enter temperature in F : "))
tem = F_to_C(f)
print(f"The temperature in Celcius is : {round(tem,1)}")

