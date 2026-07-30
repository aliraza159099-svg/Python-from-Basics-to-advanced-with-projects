#all important functions of String

name = "Raza"
#Finding length of String usinf len
print(len(name))

#Check whether string ends with and starts with
print(name.endswith("a")) #True
print(name.endswith("ka")) #False

print(name.startswith("Rz")) #False
print(name.startswith("Ra")) #True

#replace function is used to repaced words
boy = "Ali is a good boy. Ali is a Software Engineer"
print(boy.replace("Ali","Ahmed")) #Replace all the existing words with the new one