from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def bookTicket(self,fro,to):
        print(f"The train no {self.trainNo} is booked from {fro} to {to}")

    def getStatus(self):
        print(f"The bus {self.trainNo} is booked by someone")

    def getFare(self):
        print(f"The passenger got a fare of {randint(200,500)}")

p1 = Train(5908)
p1.bookTicket("Pindi","Lahore")
p1.getStatus()
p1.getFare()
