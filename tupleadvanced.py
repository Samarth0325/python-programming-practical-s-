# Employee data stored as tuples
# (Employee ID, Name, Salary)
employees = (
    (101, "Amit", 50000),
    (102, "Neha", 60000),
    (103, "Rahul", 55000),
    (104, "Priya", 70000)
)

# Function to display all employees
def display_employees(emp_data):
    for emp in emp_data:
        print(emp)

# Function to find highest salary
def highest_salary(emp_data):
    return max(emp_data, key=lambda x: x[2])

# Function to calculate total salary
def total_salary(emp_data):
    return sum(emp[2] for emp in emp_data)

print("Employee Records:")
display_employees(employees)

print("\nEmployee with Highest Salary:", highest_salary(employees))
print("Total Salary of All Employees:", total_salary(employees))
