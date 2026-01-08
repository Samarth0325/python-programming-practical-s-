# Parent class
class Animal:
    def speak(self):
        print("Animal makes sound")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating object of child
d = Dog()

# Calling parent method
d.speak()

# Calling child method
d.bark()
