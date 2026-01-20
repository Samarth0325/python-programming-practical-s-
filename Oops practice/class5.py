#In this programm we learn about modify class property inpython.

#Creating class
class Myclass:
    Lastname = "Ligade"   #Declaring class property

#defining object property
    def __init__(self,name):
        self.name = name

#creating object
p = Myclass("Samarth")

#Accessing object
print(p.name)
print(p.Lastname)

#Modifying class Property
p.Lastname = "Deshmukhe"
print(p.Lastname)

#Deleting class property using del keyword
del(p.Lastname)
del(p.name)
print()
