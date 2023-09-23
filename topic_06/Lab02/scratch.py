from Student import Student

all_students = []
student_file = open('students.txt', 'r')

for line in student_file:
    # Split the line into fields
    fields = line.strip().split(',')

    # Get named properties from each field in list
    id, first_name, last_name, qual_code = fields

    # Create student object from properties
    student = Student(id, first_name, last_name, qual_code)

    # Add to student list
    all_students.append(student)

print(all_students)
