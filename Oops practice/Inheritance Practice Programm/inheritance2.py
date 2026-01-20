# Learn how to add new properties using a child class in inheritance

# Parent class
class Person:
    def __init__(self, fname, lname):
        # Initialize first name
        self.fname = fname
        # Initialize last name
        self.lname = lname

    def display(self):
        # Display first name and last name
        print(self.fname, self.lname)


# Child class inheriting from Person
class Student(Person):
    def __init__(self, fname, lname, year):
        # Call the parent class constructor to initialize fname and lname
        super().__init__(fname, lname)

        # New property added in child class
        self.year = year

    def withyear(self):
        # Display message using parent properties and child property
        print("Welcome", self.fname, self.lname, "in the class of", self.year)


# Creating object of Child class (Student)
s = Student("Samarth", "Deshmukhe", 2025)

# Calling child class method
s.withyear()
