# Declaring a dictionary
student = {
    "name": "Samarth",
    "age": 20,
    "course": "AI & ML",
    "marks": 85
}
print("Original Dictionary:", student)

# 1. get() – Get value using key
print("Name:", student.get("name"))

# 2. keys() – Get all keys
print("Keys:", student.keys())

# 3. values() – Get all values
print("Values:", student.values())

# 4. items() – Get all key-value pairs
print("Items:", student.items())

# 5. update() – Update or add elements
student.update({"college": "AIT", "marks": 90})
print("After update():", student)

# 6. pop() – Remove a key-value pair
student.pop("age")
print("After pop('age'):", student)

# 7. popitem() – Remove last inserted key-value pair
student.popitem()
print("After popitem():", student)

# 8. setdefault() – Get value; add if not exists
student.setdefault("city", "Pune")
print("After setdefault():", student)

# 9. copy() – Copy dictionary
new_student = student.copy()
print("Copied Dictionary:", new_student)

# 10. clear() – Remove all items
new_student.clear()
print("After clear():", new_student)

# 11. len() – Number of key-value pairs
print("Length:", len(student))

# 12. fromkeys() – Create new dictionary from keys
keys = ("id", "email", "phone")
new_dict = dict.fromkeys(keys, "Not Available")
print("Fromkeys Dictionary:", new_dict)
