from StudentClass import Student

class Course():

  # Class level variables
  __valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
  __valid_times = ["0900 - 1100", "1130 - 1330", "1400 - 1600"]

  #Constructor
  def __init__(self, new_course_name="Course Name Not Set",
               new_day_of_week="Day Of Week Not Set",
               new_time="Time Not Set",
               new_room="Room Not Set",
               new_lecturer="Lecturer Not Set"):
    self.__course_name = new_course_name
    self.set_day_of_week(new_day_of_week)
    self.set_time(new_time)
    self.__room = new_room
    self.__lecturer = new_lecturer
    self.__add_students()

  def set_time(self, new_time):
    if new_time.strip() in Course.__valid_times:
      self.__time = new_time.strip()
    else:
      self.__time = "Time Not Set"

  def set_day_of_week(self, new_day_of_week):
    if new_day_of_week.strip().title() in Course.__valid_days:
      self.__day_of_week = new_day_of_week.strip().title()
    else:
      self.__day_of_week = "Day Of Week Not Set"


  def __add_students(self):
    self.__all_students = []

    with open("students.txt", "rt") as student_file:
      for line in student_file:
        id,first_name,last_name,qual_code = line.strip().split(",")
        student = Student(id.strip(), first_name.strip(), last_name.strip(), qual_code.strip())
        self.__all_students.append(student)

  def get_lecturer(self):
    return self.__lecturer

  def get_students(self):
    all_students = ""
    for student in self.__all_students:
      all_students = all_students + "\n\t" + str(student)
    return all_students

  def get_course_name(self):
    return self.__course_name

  def get_day_of_week(self):
    return self.__day_of_week

  def get_time(self):
    return self.__time

  def get_room(self):
    return self.__room

  def __str__(self):
    return (f"Course: {self.__course_name}, "
            f"Day: {self.__day_of_week}, "
            f"Time: {self.__time}, "
            f"Room: {self.__room},"
            f"\nLecturer: \n\t{self.__lecturer},"
            f"\nStudents: {self.get_students()}")
