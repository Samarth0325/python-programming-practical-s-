# Declaring a set
my_set = {10, 20, 30, 40, 50}
print("Original Set:", my_set)

# 1. add() – Add an element
my_set.add(60)
print("After add(60):", my_set)

# 2. update() – Add multiple elements
my_set.update([70, 80])
print("After update([70, 80]):", my_set)

# 3. remove() – Remove an element (error if not found)
my_set.remove(20)
print("After remove(20):", my_set)

# 4. discard() – Remove an element (no error if not found)
my_set.discard(100)
print("After discard(100):", my_set)

# 5. pop() – Remove a random element
removed = my_set.pop()
print("Removed element:", removed)
print("After pop():", my_set)

# 6. copy() – Copy the set
new_set = my_set.copy()
print("Copied Set:", new_set)

# 7. clear() – Remove all elements
new_set.clear()
print("After clear():", new_set)

# 8. union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1.union(set2))

# 9. intersection()
print("Intersection:", set1.intersection(set2))

# 10. difference()
print("Difference:", set1.difference(set2))

# 11. symmetric_difference()
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 12. issubset()
print("Is set1 subset of set2?", set1.issubset(set2))

# 13. issuperset()
print("Is set1 superset of set2?", set1.issuperset(set2))

# 14. isdisjoint()
print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))
