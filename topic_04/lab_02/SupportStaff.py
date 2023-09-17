from Staff import Staff


class SupportStaff(Staff):
    # Constructor
    def __init__(self,
                 name,
                 tel_num,
                 email,
                 new_id,
                 emp_type,
                 dept,
                 salary,
                 reporting_to,
                 level
                 ):
        super().__init__(name, tel_num, email, new_id, emp_type, dept, salary)
        self.__reporting_to = reporting_to
        self.__level = level

    # Getters
    def get_reporting_to(self):
        return self.__reporting_to

    def get_level(self):
        return self.__level

    # Setters
    def set_reporting_to(self, reporting_to):
        self.__reporting_to = reporting_to

    def set_stream(self, level):
        self.__level = level

    # Methods
    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"reporting_to: {self.__reporting_to}"
        details += f"\n\t"
        details += f"level: {self.__level}"
        details += f"\n]"
        return details
