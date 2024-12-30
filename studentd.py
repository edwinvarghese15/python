student = {}

n = int(input("Enter the number of students: "))

# Collecting data for each student
for i in range(n):
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter Grade: ")
    student[name] = (age, grade)  # Storing as a tuple (age, grade)

# Printing the information of all students
for name, (age, grade) in student.items():
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

# Printing the dictionary as it is
print(student)
