# List are just like arrays and they are mutable
#Note: In one list we can store any type of data

# List to store name of 5 numbers 
numbers = [4,5,1,34,21,9,3,67,23,54,24]
# A lots of functions we have for list manupilation as 
print(numbers[0],numbers[1]) # Using array index to print elements

#an element can be added at the end using append function
numbers.append(7)
print(numbers)

#an element can be added at specified location using insert function
numbers.insert(2,17) #at index 2 17 will be inserted the index number
# of elements on right side wil be increase by 1
print(numbers)

# List can be sorted using sort function
numbers.sort() # Here the list will be sorted and the previous list isn't
# in old state its clarly explain mutabality of list 
print(numbers)

# An element can be deleted using pop function and the element can be printed as
a = numbers.pop(4) #element at index 4 will be deleted and it is stored in a
print(a)
print(numbers)

# An element can be removed using remove function no need of index number
numbers.remove(34)
print("Removing 34 from the list")
print(numbers)

# List can be reverse using reverse function
numbers.reverse()
print(numbers)


