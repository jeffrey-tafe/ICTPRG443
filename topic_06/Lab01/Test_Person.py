from Course import Course
from Lecturer import Lecturer
from Person import Person
from Student import Student

def main():
    course = Course("Python Intermediate", "Thursday", "11:30", "Virtual")
    print(course)

    lecturer = Lecturer("123", "Danny", "Sarris", "Technology")
    print(lecturer)

    person = Person("456","Jacinda", "Smith")
    print(person)

    student = Student("789", "Jeffrey", "Smith", "Programming")
    print(student)


if __name__ == '__main__':
    main()
