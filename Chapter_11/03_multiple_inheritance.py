
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        return f"The name of the man is {self.name} and its age is {self.age}"

class GoodMan:
    fFood = "Fruits"
    def __init__(self,cha):
        self.cha = cha
    def character(self):
        return f"His character is  {self.cha} "

class Student(Human,GoodMan):
    def __init__(self, name, age,cha):
        Human.__init__(self,name, age)
        GoodMan.__init__(self,cha)


s1 = Student("Babar",23,"Good")
print(s1.info())
print(s1.character())
print(f"His favorite food is {s1.fFood}")