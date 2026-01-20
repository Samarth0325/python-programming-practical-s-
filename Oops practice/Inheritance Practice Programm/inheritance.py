# Learn about inheritance in Python:
# How to create parent and child classes

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname, self.lname)


# Child class inheriting from Person
class Student(Person):
    pass


# Creating object of Parent class
p = Person("Samarth", "Deshmukhe")
p.display()

