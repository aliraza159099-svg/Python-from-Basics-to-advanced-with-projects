# Sets: They don't repeat the elements 

# Creating sn empty set
set = { } # this is not correct way as its an empty dictionary not set
print(type(set))
#An empty set is created in this way:
# a = set()
# print(type(a)) #its working on REPL but not here

#Set don't repeat elements 
#Sets are mutable 
# any data type can be in the set

num = {3,4,5,6,7,8,3,4,"python"}
print(num) #it will not print 3 two times 

num.add(9)
print(num) # 9 will be added into the original one

