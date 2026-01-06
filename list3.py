# Creating a list with duplicate values
data = [1, 2, 3, 2, 4, 1, 5]

# Converting list to set to remove duplicates
unique_set = set(data)

# Converting set back to list
unique_list = list(unique_set)

# Printing original and updated list
print("Original List:", data)
print("List without duplicates:", unique_list)
