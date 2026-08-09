'''
In inheritance the child class can use the methods of its parent
and if the child has no constructor then the parents constructor will
be called and if the child has a constructor then using the keyword 
super.__init__() we must called the papents constructor with the 
required arguments as given below
'''
class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        print("Parents constructor is called")

    def getBasicInfo(self):
        return f"The name of the student is {self.name} and his roll no is {self.roll_no}"

class Topper(Student):
    def __init__(self, name, roll_no,position):
        self.position = position
        super().__init__(name, roll_no)
        print("Child constructor is called")
    def getInfo(self):
        return f"He is a topper his position is {self.position}"

t1 = Topper("Raza",1234,1)
a = t1.getBasicInfo()
print(a)
b = t1.getInfo()
print(b)