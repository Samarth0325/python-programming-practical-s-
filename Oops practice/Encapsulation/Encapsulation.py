#Encapsulation is about protecting data inside the class.
#In Python, encapsulation is achieved using access modifiers:

# 1. Public Members:
#    - No underscore before the variable name
#    - Can be accessed directly from outside the class
#    Example: self.brand
#
# 2. Protected Members:
#    - Single underscore (_) before the variable name
#    - Should be accessed only within the class or its child classes
#    Example: self._model
#
# 3. Private Members:
#    - Double underscore (__) before the variable name
#    - Cannot be accessed directly from outside the class
#    - Used to hide internal data
#    Example: self.__price

# Person class demonstrating Encapsulation
class Person:
    def __init__(self, name, age):
        # Public variable: can be accessed directly
        self.name = name
        
        # Private variable: cannot be accessed directly outside the class
        # Double underscore (__) makes it private
        self.__age = age

    def get_age(self):
        # Getter method
        # Used to safely access the private variable __age
        return self.__age

    def set_age(self, age):
        # Setter method
        # Used to safely modify the private variable __age
        if age > 0:          # Simple validation
            self.__age = age
        else:
            print("Age must be positive")


# Create an object of Person class
p = Person("Samarth", 21)

# Access public variable directly
print(p.name)

# Access private variable using getter method
print(p.get_age())

# Modify private variable using setter method
p.set_age(20)

# Access updated age
print(p.get_age())
