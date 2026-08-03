 
class Phone:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def call(self,caller):
        print(f"{caller} is calling.....from {self.brand} ")

p1 = Phone("iPhone",23000)
p1.call("Raza")
p2 = Phone("Samsung",34500)
p2.call("Alex")