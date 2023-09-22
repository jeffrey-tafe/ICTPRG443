from Person import Person


class Student(Person):

    # Constructor
    def __init__(self, new_id, first_name, last_name, qual_code):
        super().__init__(new_id, first_name, last_name)
        self.__qual_code = qual_code

    # Getters
    def get_qual_code(self):
        return self.__qual_code

    # To string override
    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\tQual Code: {self.__qual_code}"
        details += f"\n]"
        return details


# Example instantiation
# student = Student("test", "Jeffrey", "Smith", "Programming")
# print(student)
