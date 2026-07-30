#Abstring is used here

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Good morning,{name}.Youa re {age} years old")


# Repalce words in any string using replace function
para = '''
Author XYZ
Pakistan is of the most varnarable country to Global Warming.
Date ABC
'''
author = input("Enter author name: ")
date  = input("Enter the date: ")

print(para.replace("XYZ",author).replace("ABC",date))


