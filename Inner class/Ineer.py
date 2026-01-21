# Inner class means Parent class inside the parent class.

#In this program we learn about accessing Inner class from Outer Class.

class Outer:
    def __init__(self):
        self.name = "outer"

    # Inner (nested) class
    class Inner:
        def __init__(self):
            self.name = "inner"


# Create object of Outer class
outer = Outer()

# Create object of Inner class
# Inner is accessed using the Outer class
inner = Outer.Inner()

# Access attributes
print(outer.name)   # Output: outer
print(inner.name)   # Output: inner
