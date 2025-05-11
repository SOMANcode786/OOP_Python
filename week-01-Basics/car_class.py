class car:

    def __init__(self,make,model,year,color):
        '''Initialize the car with make, model, year, and color.'''
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        '''Display the car's information.'''

    def display(self):
        print(f"Make: {self.make} , Model : {self.model} ,Year : {self.year}, Color : {self.color}")

car1=car("Toyota " , "Corolla", 2020, "Red")
car1.display()