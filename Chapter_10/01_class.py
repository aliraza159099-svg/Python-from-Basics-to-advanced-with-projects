
class Employee:
    Name = "Ali Raza"
    salary = 1230000

e1 = Employee()
print(e1.Name, e1.salary)
with open("employ.txt","w") as f:
    f.write(e1.Name, e1.salary)