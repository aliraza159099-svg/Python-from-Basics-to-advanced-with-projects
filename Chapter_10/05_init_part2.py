
class Employee():
    def __init__(self,name,age,address):
        print("An object has been created")
        self.name = name
        self.age = age
        self.address = address

    def getInfo(self):
        print(f"The name of the employe is : {self.name}\nHis age is : {self.age}\nHe is from : {self.address}")

e1 = Employee("Raza",20,"Baltistan")
e1.getInfo()