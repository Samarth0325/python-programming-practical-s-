# In this programm we learn about what is function in class how we can use it as a method for getting an output which we want.


#Creating class
class Car:

    #defining Object properties
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Displaying function as a method to get output as we want 
    def display(self):
        print(f"I have a car of brand {self.brand} who's model is {self.model} i buy it in year {self.year}.")

#Creating object of class
p = Car("Toyota","Fortuner",2030)

#Accessing probperties by accessing defined function
p.display()
