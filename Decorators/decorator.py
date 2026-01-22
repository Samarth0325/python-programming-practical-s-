# Decorator function
# It takes another function as an argument
def changecase(fun):

    # Inner function (wrapper)
    # This function adds extra behavior to the original function
    def myinner():
        # Call the original function and store its returned value
        result = fun()
        
        # Convert the returned string to uppercase and print it
        print(result.upper())

    # Return the inner function instead of calling it
    return myinner


# Using the decorator syntax
# This replaces my_function with the myinner function
@changecase
def my_function():
    # Original function returns a string
    return "hello"


# Calling the decorated function
# It will execute the code inside myinner()
my_function()
