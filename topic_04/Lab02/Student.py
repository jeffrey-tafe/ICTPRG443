from Person import Person

class Student(Person):

    # Constructor
    def __init__(self,
                 name,
                 tel_num,
                 email,
                 new_id,
                 date_enrolled,
                 program_enrolled,
                 student_type):
        super().__init__(name, tel_num, email, new_id)
        self.__date_enrolled = date_enrolled
        self.__program_enrolled = program_enrolled
        self.__type = student_type

    # Getters
    def get_date_enrolled(self):
        return self.__date_enrolled

    def get_program_enrolled(self):
        return self.__program_enrolled

    def get_type(self):
        return self.__type

    # Setters
    def set_date_enrolled(self, date):
        self.__date_enrolled = date

    def set_program_enroll(self, program):
        self.__program_enrolled = program

    def set_type(self, student_type):
        self.__type = student_type

    # Methods
    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"date_enrolled: {self.__date_enrolled}"
        details += f"\n\t"
        details += f"program_enrolled: {self.__program_enrolled}"
        details += f"\n\t"
        details += f"type: {self.__type}"
        details += f"\n]"
        return details
