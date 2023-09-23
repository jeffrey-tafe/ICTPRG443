from Student import Student


class Course:

    # Constants
    __VALID_DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    __VALID_CLASS_TIMES = ["0900-1100", "1130-1330", "1400-1600"]

    # Constructor
    def __init__(self, course_name, day_of_week, time, room, lecturer):
        self.__course_name = course_name
        self.set_day_of_week(day_of_week)
        self.set_time(time)
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

    # Setters
    def set_day_of_week(self, day):
        if day.strip().title() not in Course.__VALID_DAYS_OF_WEEK:
            self.__day_of_week = "Day Of Week Not Set"
        else:
            self.__day_of_week = day.title()

    def set_time(self, time):
        if time.strip() in Course.__VALID_CLASS_TIMES:
            self.__time = time.strip()
        else:
            self.__time = "Time Not Set"

    # Methods
    def __add_students(self):
        self.__all_students = []

        # Open student file with context manager
        with open('students.txt', 'r') as student_file:
            for line in student_file:

                # Split the line into fields
                fields = line.strip().split(',')

                # Get named properties from each field in list
                id, first_name, last_name, qual_code = fields

                # Create student object from properties
                student = Student(id, first_name, last_name, qual_code)

                # Add to student list
                self.__all_students.append(student)

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
