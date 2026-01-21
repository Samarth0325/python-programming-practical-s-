#The word polymorphism means many forms.
#In programming we refer that as a function/method/operators.
#That are with the same names but we can execute each for as a sane name for different objects or classes.

#In this programm we learn about how polymorphism work in python where we have multiple classes
#and we execute it using same method.


#creating class
class Car:
    def __init__(self,brand,model):
        self.brand =  brand
        self.model = model

#Defining function
    def move(self):
        print("drive")

#creating class
class Boat:
     def __init__(self,brand,model):
        self.brand =  brand
        self.model = model

#Defining function
     def move(self):
         print("drive")

#Creating object for calling properties for each class
car = Car("Maruti",300)
boat = Boat("Hyundai",100)

#Using for loop for accessing propreties of both classes.
for i in (car,boat):
    i.move()