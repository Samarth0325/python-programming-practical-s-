#learn about how to return argument in form of more than one key value using **argument form.

def my_function(**kid): #**argument using this form we declare more than one argument.
    print("His last name is"+kid["lname"])
my_function(fname="sam",lname="deshmukhe") #we define many arguments.