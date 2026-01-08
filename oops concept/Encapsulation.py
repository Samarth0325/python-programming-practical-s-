class Bank:
    def __init__(self):
        self.__balance = 5000   # Private variable

    # Public method to access private data
    def get_balance(self):
        print("Balance:", self.__balance)

# Creating object
b1 = Bank()

# Accessing balance using method
b1.get_balance()
