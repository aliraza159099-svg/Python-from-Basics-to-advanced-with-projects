
class student:
    school = "Uswa College Islamabad" #these are the class attributes
    year = 2026

s1 = student()
print(s1.school,s1.year) #These are the class attributes 

s1.name = "Ali Raza" #this is an instance attribute
print(s1.name,s1.school,s1.year) 

s2 = student()
print(s2.school,s2.year) #These are the class attributes 

s2.name = "Kabir Ali" #this is an instance attribute
print(s2.name,s2.school,s2.year) 