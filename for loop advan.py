# AI Student Result Processing System
# For Loop Based Mini Project

students = int(input("Enter number of students: "))

names = []
marks_list = []
percentages = []
grades = []

# Step 1: Input student data
for i in range(students):
    print("\nEnter details of Student", i+1)
    name = input("Enter name: ")
    marks = []

    # Taking 5 subject marks
    for j in range(5):
        mark = float(input(f"Enter marks for Subject {j+1}: "))
        marks.append(mark)

    names.append(name)
    marks_list.append(marks)

# Step 2: Calculate percentage for each student
for i in range(students):
    total = 0
    for m in marks_list[i]:
        total += m

    percentage = total / 5
    percentages.append(percentage)

    # Step 3: Assign grade using conditions
    if percentage >= 85:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    grades.append(grade)

# Step 4: Display student results
print("\n------- STUDENT RESULT REPORT -------")
for i in range(students):
    print("Name:", names[i])
    print("Percentage:", round(percentages[i], 2))
    print("Grade:", grades[i])
    print("-----------------------------------")

# Step 5: Find Topper
topper_index = 0
for i in range(1, students):
    if percentages[i] > percentages[topper_index]:
        topper_index = i

print("\n🏆 Topper of the Class 🏆")
print("Name:", names[topper_index])
print("Percentage:", round(percentages[topper_index], 2))
