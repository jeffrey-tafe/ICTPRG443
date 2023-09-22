class Course:

    # Constructor
    def __init__(self, course_name, day_of_week, time, room):
        self.__course_name = course_name
        self.__day_of_week = day_of_week
        self.__time = time
        self.__room = room

    # Getters
    def get_course_name(self):
        return self.__course_name

    def get_day_of_week(self):
        return self.__day_of_week

    def get_time(self):
        return self.__time

    def get_room(self):
        return self.__room

    # To string override

    def __str__(self):
        details = f"\n{super().__str__()}"
        details += f"\n["
        details += f"\n\tCourse Name: {self.__course_name}"
        details += f"\n\tDay Of Week: {self.__day_of_week}"
        details += f"\n\tTime: {self.__time}"
        details += f"\n\tRoom: {self.__room}"
        details += f"\n]"
        return details


# Example instantiation
# course = Course("Python Intermediate", "Thursday", "11:30", "Virtual")
# print(course)
