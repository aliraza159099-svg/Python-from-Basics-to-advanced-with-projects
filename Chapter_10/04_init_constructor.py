# Constartuctor are made to instanciate the objetc easily

class Students():
    def __init__(self,name,Class,rollno):
        print("An object is creating")
        self.name = name
        self.Class = Class
        self.rollno = rollno
        print(f"The name of the sudent is : {name}\nHe is in class : {Class}\nHis roll no is : {rollno}")


s1 = Students("Rohan","5th",567) #When an obj is created the init is called

