
class Demo():
    a = 8

d1 = Demo()
print(d1.a) #print the class attribute of Demo where a = 8
d1.a = 0 #The attribute of the d1 object is set to 0
print(d1.a)
print(Demo.a) #But the class attribute isn't change