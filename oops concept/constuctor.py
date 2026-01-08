class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    # Method to show details
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Object creation
s1 = Student("Shreyash", 21)

# Calling method
s1.show()
