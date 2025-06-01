class Atm:  
    def __init__(self,balance, pin):
        self.balance =balance
        self.pin = ""
        self.display()


    def display(self):
        print(f"Balance: {self.balance} , Pin : {self.pin}")


atm1 = Atm(1000, "1234")
