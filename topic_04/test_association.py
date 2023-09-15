from student_class import Student
from address_class import Address
from lecturer_class import Lecturer

def main():

  # AGGREGATION
  address1 = Address("101 High Street", "Adelaide", 5000)
  student1 = Student("Joe Bloggs", address1)
  student2 = Student("Jeffrey Smith", address1)

  print(student1)
  print(student2)

  # COMPOSITION
  lecturer1 = Lecturer("John Smith", "120 Crrie Street", "Adelaide", "5000")
  print(lecturer1)

main()