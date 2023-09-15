from ex01_student_class import Student

def main():
  student1 = Student("1001", "Peter Jones", "pj@pjs.com")
  student2 = Student("1002")

  print(student1)


  student1.set_id("1111")
  student1.set_name("Jeffrey Smith")
  student1.set_email("jeff@jeff.com")

  print(student1)

  print(student2)

  print(student2)

main()
