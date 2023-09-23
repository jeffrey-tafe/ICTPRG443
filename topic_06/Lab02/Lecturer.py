from Person import Person


class Lecturer(Person):

    # Constructor
    def __init__(self, new_id, first_name, last_name, work_group):
        super().__init__(new_id, first_name, last_name)
        self.__work_group = work_group

    # Getters
    def get_work_group(self):
        return self.__work_group

    # To string override
    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\tWork Group: {self.__work_group}"
        details += f"\n]"
        return details


# Example instantiation
# lecturer = Lecturer("123", "Danny", "Sarris", "Technology")
# print(lecturer)
