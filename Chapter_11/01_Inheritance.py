
class Employee:
    company = "Raza Tech"
    def __init__(self,name):
        # print("Parent is called")
        self.name = name

    def getInfo(self):
        return f"The employee is {self.name}"

class Programmer(Employee):
    def __init__(self, name):
        super().__init__(name)

p1 = Programmer("Raza")
print(p1.getInfo())