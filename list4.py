# Student Marks Analysis using List

# List of student marks
marks = [78, 85, 62, 90, 55, 88, 76, 95, 67]

# Function to calculate average
def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

# Function to find highest and lowest marks
def find_max_min(marks_list):
    return max(marks_list), min(marks_list)

# Function to count passed students (>=60)
def count_passed(marks_list):
    return len([m for m in marks_list if m >= 60])

# Perform operations
average = calculate_average(marks)
highest, lowest = find_max_min(marks)
passed_students = count_passed(marks)

# Display results
print("Student Marks:", marks)
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Number of Passed Students:", passed_students)
