# A lambda function is a small anonymous function in Python.
# It is defined using the 'lambda' keyword.
#
# Lambda functions can have many number of arguments,
# but only ONE expression.
#
# The result of the expression is automatically returned.
# (No need to use the 'return' keyword)
#
# Syntax:
# lambda arguments : expression

x = lambda a,b : a*b+10
print(x(5,6))