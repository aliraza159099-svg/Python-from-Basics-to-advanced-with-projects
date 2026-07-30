'''
return give a value or any string if any variable wants sth 
from the function as
'''
def greet(name):
    print(f"Good Morning {name}")
    return "welcome " 

greet("Ali")
a = greet("Bari") # Now the return value will stoe in the variable a
print("Return value is : ",a)