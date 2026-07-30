# Tuple is also a list of elements but it is immutable 
a = () #An empty tuple
print(type(a))

b = (2,) #Tuple having 1 element b = (1) is an int 
print(type(b))

c = (3) # its an int
print(type(c))

# Can an element of tuple be changed?
names = ("Ali","Rohan","Abbas","Kabir","Nadir","Haza")
# names[4] = "Ahmed"
print(names) #Its not possible beacuse tuple are immutable

