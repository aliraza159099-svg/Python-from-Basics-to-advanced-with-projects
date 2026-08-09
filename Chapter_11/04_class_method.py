
# The keyword classmethod is use to use the class sttribute not the obj attributes 
class Animal:
    age = 12

    @classmethod
    def showAge(cls):
        print(f"The age of the animal is {cls.age}")


a1 = Animal()
a1.age = 10
a1.showAge()

