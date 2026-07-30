'''if we don't provide the ending from function calling 
it will print the default ending else it will print the provided parameter

'''

def greet(name,ending="Thank you "):
    print(name)
    print(ending)

greet("Ali Raza")

greet("Rohan Kumar","Aap ka Shukurya ")