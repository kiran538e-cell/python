# Take dictionary of five students includding name:marks as "key":value , use for loop to iterate and if elif and else to assign grades.
# 1. Dictionary: Storing names and marks of 5 students
student = {"Ali": 85, "Ayesha":92, "Zain":99, "Fatima": 68, "Bilal": 81}

# For Loop: Iterating through each student name in the dictionary
for name in student:
    
    # Logic to fetch the marks of the current student that we need in if, elif, else
    marks = student[name] 
    if marks >= 90:                             #If/Elif/Else Logic: Checking marks to assign the correct grade
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "F"
    print("Student:", name, " |  Marks:", marks, " |  Grade:", grade)