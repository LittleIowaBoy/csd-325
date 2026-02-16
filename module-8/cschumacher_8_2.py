

import json

def print_student_list(student_list):
    # Function to loop through and print each student
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load the JSON file into a Python list
with open('Student.json', 'r') as file:
    students = json.load(file)

# Print original student list
print("--- Original Student List ---")
print_student_list(students)


# Add new student to the list
new_student = {
    "F_Name": "Caleb",
    "L_Name": "Schumacher",
    "Student_ID": 9999999,
    "Email": "cschumacher@my365.bellevue.edu"
}
students.append(new_student)

# Print updated student list
print("--- Updated Student List ---")
print_student_list(students)


# Write the updated list back to the JSON file
with open('Student.json', 'w') as file:
    json.dump(students, file, indent=4)

print("--- The Student.json file has been updated ---")
