# In this program, we learn how to use the __init__() method in a child class.
# And also learn about how to use suoer(). method for accessing parent class properties in chilad class.

# Parent class
class Person:
    def __init__(self, fname, lname):
        # Initialize first name
        self.fname = fname
        # Initialize last name
        self.lname = lname

    def display(self):
        # Display full name
        print(self.fname, self.lname)


# Child class inheriting from Person
class Student(Person):
    def __init__(self, fname, lname):
        # Call the parent class __init__() method
        # to initialize fname and lname
        super().__init__(fname, lname)


# Creating object of Parent class
p = Person("Samarth", "Deshmukhe")

# Calling display method of Person class
p.display()
