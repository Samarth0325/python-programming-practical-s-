import array as arr

# Creating an array
numbers = arr.array('i', [10, 20, 30, 40])

# Inserting element at index 2
numbers.insert(2, 25)

# Displaying updated array
print("Array after insertion:", numbers)
