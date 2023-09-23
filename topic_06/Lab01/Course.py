from Student import Student

class Course:

    # Constructor
    def __init__(self, course_name, day_of_week, time, room, lecturer):
        self.__course_name = course_name
        self.__day_of_week = day_of_week
        self.__time = time
        self.__room = room
        self.__lecturer = lecturer
        self.__add_students()

    # Getters
    def get_course_name(self):
        return self.__course_name

    def get_day_of_week(self):
        return self.__day_of_week

    def get_time(self):
        return self.__time

    def get_room(self):
        return self.__room

    def get_lecturer(self):
        return self.__lecturer

    def get_students(self):
        return self.__all_students

    # Methods
    def __add_students(self):
        self.__all_students = []
        stud1 = Student("001", "Jimmy", "Little", "MUSIC101")
        stud2 = Student("002", "Bill", "Burr", "COMEDY101")
        self.__all_students.append(stud1)
        self.__all_students.append(stud2)

    # To string override

    def __str__(self):
        details = f"\n{super().__str__()}"
        details += f"\n["
        details += f"\n\tCourse Name: {self.__course_name}"
        details += f"\n\tDay Of Week: {self.__day_of_week}"
        details += f"\n\tTime: {self.__time}"
        details += f"\n\tRoom: {self.__room}"
        details += f"\n\tLecturer: {self.__lecturer}"

        # Build string of student array details
        student_string = ""
        for student in self.__all_students:
            student_string += student.__str__()

        details += f"\n\tStudents: {student_string}"
        details += f"\n]"
        return details


# Example instantiation
# course = Course("Python Intermediate", "Thursday", "11:30", "Virtual")
# print(course)
