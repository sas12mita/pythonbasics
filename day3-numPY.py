import numpy as np

# Step 1: Create the marks array (5 students, 3 subjects)
marks = np.array([
    [78, 85, 90],   # Student 1
    [92, 88, 76],   # Student 2
    [65, 70, 60],   # Student 3
    [80, 75, 85],   # Student 4
    [90, 95, 92]    # Student 5
])

# Step 2: Slice the Data
student2 = marks[1]              # All marks of Student 2
science_marks = marks[:, 1]     # All Science marks
math_first3 = marks[:3, 0]      # Math marks of first 3 students

# Step 3: Do Math Operations
marks[:, 2] += 5                # Add 5 bonus marks to English (3rd column)
total = np.sum(marks, axis=1)  # Total marks per student
avg_per_subject = np.mean(marks, axis=0)  # Average per subject

# Step 4: Analyze Results
highest = np.max(total)                  # Highest total marks
lowest_index = np.argmin(total)         # Index of student with lowest total

# Display the results
print("Marks:\n", marks)
print("\nStudent 2's marks:", student2)
print("Science Marks:", science_marks)
print("Math marks of first 3 students:", math_first3)
print("\nTotal Marks per Student:", total)
print("Average Marks per Subject:", avg_per_subject)
print("Highest Total Marks:", highest)
print("Lowest Scorer: Student", lowest_index + 1)
