class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

# Creating objects
d = Dog()
c = Cat()

# Same method name but different behavior
d.sound()
c.sound()
