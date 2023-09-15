from TafePersonClass import TafePerson
from StudentClass import Student
from LecturerClass import Lecturer
from CourseClass import Course

def main():



  person1 = TafePerson("P123", "Peta", "Jones")
  print(person1)

  lecturer1 = Lecturer("l123", "John", "Smith", "IT Studies")
  print (lecturer1)

  course1 = Course("PRG443PYI", "Thursday1", "1130 - 1330", "Virtual", lecturer1)
  print(course1)

if __name__ == '__main__':
  main()