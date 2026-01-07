# AI-Based Student Performance Analyzer
# Uses advanced conditional statements (if-elif-else)

# Taking input from the user
name = input("Enter Student Name: ")
marks = float(input("Enter Exam Marks (out of 100): "))
attendance = float(input("Enter Attendance Percentage: "))
assignment = float(input("Enter Assignment Score (out of 100): "))

# Calculating final weighted score
final_score = (marks * 0.6) + (attendance * 0.2) + (assignment * 0.2)

print("\n----- Student Performance Report -----")
print("Student Name:", name)
print("Final Score:", round(final_score, 2))

# Using conditional statements for performance classification
if final_score >= 85:
    grade = "Excellent"
    recommendation = "Eligible for scholarship and advanced AI training."
elif final_score >= 70:
    grade = "Good"
    recommendation = "Can be considered for internship opportunities."
elif final_score >= 50:
    grade = "Average"
    recommendation = "Needs improvement through additional practice."
else:
    grade = "Needs Improvement"
    recommendation = "Requires mentoring and remedial classes."

# Displaying result
print("Performance Level:", grade)
print("AI Recommendation:", recommendation)
