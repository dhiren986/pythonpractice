import re
students = {
    "Alice": 83,
    "Dhiren": 97,
    "Bob": 76,
    "Charlie": 50,
}
name= input("Enter the student's name: ")
found = False
for student in students:
    if re.search(name, student, re.IGNORECASE):
        print(f"{student}'s marks: {students[name]}")
        found = True

if not found:
    print("Student not found.")
