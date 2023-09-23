from Course import Course
from Lecturer import Lecturer
from Person import Person


def main():


    lecturer = Lecturer("123", "Danny", "Sarris", "Technology")
    # print(lecturer)

    person = Person("456","Jacinda", "Smith")
    # print(person)

    # student1 = Student("001", "Jeffrey", "Smith", "Programming")
    # student2 = Student("002", "Jack", "Bucksin", "Programming")
    # student3 = Student("003", "Kylie", "Farro", "Programming")
    # student4 = Student("004", "Rhiannon", "Rearden", "Programming")
    # student5 = Student("005", "Louise", "Lamora", "Programming")
    # students = [student1, student2, student3, student4, student5]

    course = Course("Python Intermediate", "Thursday", "11:30", "Virtual", lecturer)
    print(course)


if __name__ == '__main__':
    main()
