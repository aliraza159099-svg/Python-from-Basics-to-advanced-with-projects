# Various type of methods we have for tuples
num = (12,32,34,54,23,43,54,65,11,6,8,12)
# Using count we can count the number of particular element in the tuple
print(num.count(12))

# Using index print the index of first element in the tuple
print(num.index(34),num.index(12)) #for 12 it will print only 0 as its the first index
#two tuples can form a new one by concatenation but the originals won't change
tuple1 = ("Ali","Ahmed","Nadir")
tuple2 = ("Raza","Kumail","Abbas")
tuple3 = tuple1 + tuple2
print(".........Tuple Concatenation........")
print(tuple1)
print(tuple2)
print(tuple3)

# Tuples can by rpeated using * operator as
tup = tuple1*3
print(tup) #Tuple1 will print 3 times

# Membership can be check using in keyword
print("Nadir" in tuple1) #return True
print("Sahil Bhatti" in tuple1) #return False

# Maximum an mininum in tuple can be printed
print("Printing the max and min in :num = (12,32,34,54,23,43,54,65,11,6,8,12) ")
print("Minimum: ",min(num))
print("Maximum: ",max(num))

#numbers can be added to print its sum
print("Sum of numbers: ",sum(num))