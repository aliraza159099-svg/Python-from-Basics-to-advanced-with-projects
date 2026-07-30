# Items of  dictionary is printed using item method

student = {
  "Ali" : 20,
  "Raza" : 17,
  "Sadam" : 23
}
#A copy s made to get the original anywhere in the code
copied_dictionary = student.copy()
print(student.items()) #Will print all in the form of tuple

# Keys can be printed using key method
print(student.keys()) # Will print the keys of dictonary

print(student.values()) # Will print the values of the dictionay

# Values can be updated using update method
student.update({"Ali":19}) #original dictionary will be changed
print(student)

# Also new key values can be added using same method
student.update({"Ahmed": 9})
print(student) #Ahmed is added in the dictionary

# Values of keys can be find using get using get function
# It will print none if key isn't in the dictionary
# default value can be set
student.setdefault("Karim","Not in our record")
print(student.get("Ali")) #print age of Ali
print(student.get("Karim")) # will print none as Karim is not in the dictionary
# But the below way is also use to print the values of Keys but they throw error if
# key in absent
# print(student["Karim"])

# Dictionary van be cleared using clear method
# student.clear()
print(student)

student.pop("Ali") #Will delete Ali and his value from the dictionary
print(student)

# To print the original coped here in copied version
print("..........Original is saved here..........")
print(copied_dictionary)



