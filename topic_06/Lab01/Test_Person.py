from Course import Course
from Lecturer import Lecturer
from Person import Person


def main():


    lecturer = Lecturer("123", "Danny", "Sarris", "Technology")
    # print(lecturer)

    course = Course("Python Intermediate", "Thursday", "11:30", "Virtual", lecturer)
    print(course)


if __name__ == '__main__':
    main()
