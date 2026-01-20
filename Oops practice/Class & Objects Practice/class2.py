# In this program we learn about class properties in Python

# Initialization of class with inializing properties by using _init_()method.
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating object of the class
p = MyClass("Samarth", 21)

# Accessing class properties
print(p.name)
print(p.age)

# Modification of properties
p.age = 30
p.name = "Sam"

# Accessing properties again
print(p.age)
print(p.name)

# Deletion of properties using del keyword
del(p.age)
print(p.name)
