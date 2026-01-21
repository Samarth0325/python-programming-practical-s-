#In this programm we learn about how polymorphism works for Inheritance.
#Means we learn for in inheritance we define Class inside a class.
#So we learn about how we can use same method for accessing each class.

# Parent class (Base class)
class Vehicle:
    def __init__(self, brand, model):
        # Initialize common properties for all vehicles
        self.brand = brand
        self.model = model

    def move(self):
        # Default move behavior for a vehicle
        print("drive")
        

# Child class (Derived class) inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        # Call the constructor of the parent class
        # This avoids code duplication
        super().__init__(brand, model)

    def move(self):
        # Override the move() method of Vehicle class
        # This is an example of method overriding (Polymorphism)
        print("sail")


# Create a list containing one Car object
# Using a list allows us to loop through objects
car = [Car("Ford", "Mustang")]

# Loop through the list of car objects
for x in car:
    # Access the brand attribute of the Car object
    print(x.brand)

    # Access the model attribute of the Car object
    print(x.model)

    # Call the overridden move() method of Car class
    x.move()
