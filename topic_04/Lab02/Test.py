from Person import Person
from Student import Student
from Staff import Staff
from AcademicStaff import AcademicStaff
from SupportStaff import SupportStaff

print("\nTesting Person class")
person = Person("Jeffrey", "123654", "jeff@jeff.com", "0001")
print(person)

print("\nTesting Student subclass")
student = Student("Jeffrey",
                  "123654",
                  "jeff@jeff.com",
                  "0001",
                  "20230917",
                  "Python Intermediate",
                  "Part Time")
print(student)

print("\nTesting equality between student and person")
print(f"Result: {person.__eq__(student)} (Should be true)")

print("\nTesting Staff class")
staff = Staff("Jacinda",
              "987456",
              "jacinda@jacinda.com",
              "0002",
              "Full Time",
              "Executive",
              "2,000,000"
              )
print(staff)

print ("\nTesting AcademicStaff class")
academic_staff = AcademicStaff("Alandra",
                               "777888",
                               "a@a.a",
                               "0004",
                               "Part Time",
                               "Physics",
                               "1,500,000",
                               "Masters Degree",
                               "Physics",
                               "Lecturer"
                               )
print(academic_staff)

print ("\nTesting SupportStaff class")
academic_staff = SupportStaff("Jamie",
                              "321456987",
                              "j@j.j",
                              "0005",
                              "Full Time",
                              "Technology",
                              "750,000",
                              "Jacinda",
                              "4"
                              )
print(academic_staff)
