
class Employee():
    company = "XYZ..."
    year = 2026
    salary = 10000
    name = "unknown"
    # This is a method here difined as function
    def getInfo(self):
        print(f"The name of the emloye is {self.name}, he has \n{self.salary} slary and he works at {self.company}")
    @staticmethod #declaring that this method will not take anything from the obj
    def greet():
        print("Good Morning erveryone")

e1 = Employee()
e1.name = "Ali " 
e1.getInfo()
e1.greet()

