# Declaring a tuple
my_tuple = (10, 20, 30, 40, 20, 50)
print(my_tuple)

# 1. count() – Count how many times an element appears
print("Count of 20:", my_tuple.count(20))

# 2. index() – Find index of an element
print("Index of 40:", my_tuple.index(40))

# 3. len() – Length of tuple
print(len(my_tuple))

# 4. max() – Maximum value
print("Maximum:", max(my_tuple))

# 5. min() – Minimum value
print("Minimum:", min(my_tuple))

# 6. sum() – Sum of all elements
print("Sum:", sum(my_tuple))

# 7. Slicing
print("Slice from index 1 to 4:", my_tuple[1:4])

# 8. Concatenation
new_tuple = my_tuple + (60, 70)
print("After concatenation:", new_tuple)

# 9. Repetition
repeat_tuple = my_tuple * 2
print("After repetition:", repeat_tuple)

# 10. Membership
print("Is 30 in tuple?", 30 in my_tuple)

# 11. Iteration
print("Elements in tuple:")
for item in my_tuple:
    print(item)
