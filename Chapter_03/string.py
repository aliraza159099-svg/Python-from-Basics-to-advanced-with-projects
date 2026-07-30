
# Anything written inside the "...." is known as string 

a = "Ali Raza"

b = "123"

c = "67#$57" #all these are the example of String

print(a,b,c)

#String can be write in three ways with '' " " and with ''''''

name = "Safullah"
sname = name[0:3] #index number is use to make slice of string 
tname = name[3:8]

print(name,sname,tname)

#length of String as
print("the length of String is: ",len(name))

#Slicing with Skip Value
#a[1:8:5] its simply means to choose from index 
# 1 to 7 and then print first number from chosen
#  list and to jump 5 till the end of chosen list

z = "abcfgdehijklmnopqrstuvwxyz"

print(z[2:20:2])

print(z[3:25:5])