# A generator is a special type of function that returns values
# one at a time using the 'yield' keyword instead of 'return'.
#
# Generators are used to generate a sequence of values without
# storing all values in memory at once (memory efficient).
#
# When a generator function is called, it does not execute immediately.
# It returns a generator object.
#
# Each time 'next()' is called on the generator object,
# the function resumes execution from where it last stopped.
#
# The 'yield' keyword pauses the function and saves its state.

#code

def numbers(n):
    for i in range(n):
        yield i

get = numbers(100)
print(next(get))
print(next(get))

