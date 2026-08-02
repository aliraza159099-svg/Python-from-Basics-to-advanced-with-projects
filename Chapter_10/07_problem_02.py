class calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"the square of {self.num} is = {self.num * self.num}")

    def root(self):
            print(f"the root of {self.num} is = {self.num**(1/2)}")
option = 1
while option!=0:
    num = int(input("Enter your number : "))
    a = calculator(num)
    print("Enter 1 for square\nEnter 2 for square root \nEnter 0 to exit")
    option = int(input("Enter your chioce : "))
    if option == 1:
        a.square()
    elif option == 2:
        a.root()
    else:
        print("Enter a valid input")
