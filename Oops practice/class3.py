# Learn about Object properties and class properties.

#Defining class
class Myclass:

    #Defining class property outside the init method but inside the class
    species = "Human"

    #Defining class property inside the init() methosd.
    def __init__(self,name):
        self.name = name

#Creating object by valueing object property
p=Myclass("Samarth")

#Accessing properties
print(p.name)
print(p.species)