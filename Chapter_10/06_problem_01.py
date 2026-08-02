''' Making a system to store the basic information 
of the employees at Microsoft'''

class Employee_at_Microsoft:
    def __init__(self,name,salary,address):
        self.name = name
        self.salary = salary
        self.address = address
        self.details = f"The employee {name} has {salary} salary and he is from {address}\n"
        with open("MS_employee.txt","a") as f:
                    f.write(self.details)

def addEmployee():
    name = input("Enter the name of the employee : ")
    salary = int(input("Enter the slary : "))
    address = input("Enter the address : ")
    return Employee_at_Microsoft(name,salary,address)

e1 = addEmployee()