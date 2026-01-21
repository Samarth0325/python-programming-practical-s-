# Inner class means a class defined inside another class (Outer class)
# In this program, we learn how to access Outer class data from Inner class

class Outer:
    def __init__(self):
        # Attribute of Outer class
        self.name = "outer"

    # Inner (nested) class
    class Inner:
        def __init__(self, outer):
            # Store reference of Outer class object
            self.outer = outer
            self.name = "inner"

        def show_outer_name(self):
            # Access Outer class attribute using reference
            print(self.outer.name)


# Create object of Outer class
outer = Outer()

# Create object of Inner class
# Pass the outer object to Inner class
inner = Outer.Inner(outer)

# Access attributes
print(outer.name)   # Output: outer
print(inner.name)   # Output: inner

# Access Outer class attribute from Inner class
inner.show_outer_name()  # Output: outer
