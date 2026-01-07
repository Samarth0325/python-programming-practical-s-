
# Dictionary to store student data
# Roll No -> (Name, Marks)
students = {
    1: ("Amit", 85),
    2: ("Neha", 92),
    3: ("Rahul", 78),
    4: ("Priya", 88)
}

# Function to display students
def display_students(data):
    print("\nStudent Records:")
    for roll, info in data.items():
        print("Roll:", roll, "Name:", info[0], "Marks:", info[1])

# Function to add a new student
def add_student(data, roll, name, marks):
    data[roll] = (name, marks)

# Function to find topper
def find_topper(data):
    return max(data.items(), key=lambda x: x[1][1])

# Function to calculate class average
def class_average(data):
    total = sum(info[1] for info in data.values())
    return total / len(data)

# Adding a new student
add_student(students, 5, "Karan", 90)

display_students(students)

topper = find_topper(students)
print("\nTopper:", topper[1][0], "with", topper[1][1], "marks")

print("Class Average:", round(class_average(students), 2))
