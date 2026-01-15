# Declaring a list of strings
fruits = ["apple", "banana", "mango", "orange", "banana"]
print("List:", fruits)

# 1. append() – Add one element at the end
fruits.append("grapes")
print(fruits)

# 2. extend() – Add multiple elements
fruits.extend(["kiwi", "pineapple"])
print(fruits)

# 3. insert() – Insert element at a specific index
fruits.insert(2, "cherry")
print(fruits)

# 4. remove() – Remove first occurrence of element
fruits.remove("banana")
print(fruits)

# 5. pop() – Remove element at given index
fruits.pop(3)
print(fruits)

# 6. index() – Find index of an element
print(fruits.index("mango"))

# 7. count() – Count occurrences
print(fruits.count("banana"))


# 8. sort() – Sort list alphabetically
fruits.sort()
print(fruits)

# 9. reverse() – Reverse the list
fruits.reverse()
print(fruits)

# 10. copy() – Copy the list
new_fruits = fruits.copy()
print(new_fruits)

# 11. clear() – Remove all elements from copied list
new_fruits.clear()
print(new_fruits)

# 12. len() – Find length of list
print(len(fruits))

# 13. max() – Alphabetically highest element
print(max(fruits))

# 14. min() – Alphabetically smallest element
print(min(fruits))
