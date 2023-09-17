from Staff import Staff


class AcademicStaff(Staff):
    # Constructor
    def __init__(self,
                 name,
                 tel_num,
                 email,
                 new_id,
                 emp_type,
                 dept,
                 salary,
                 academic_quals,
                 stream,
                 academic_role):
        super().__init__(name, tel_num, email, new_id, emp_type, dept, salary)
        self.__academic_quals = academic_quals
        self.__stream = stream
        self.__academic_role = academic_role

    # Getters
    def get_academic_quals(self):
        return self.__academic_quals

    def get_stream(self):
        return self.__stream

    def get_academic_role(self):
        return self.__academic_role

    # Setters
    def set_academic_quals(self, quals):
        self.__academic_quals = quals

    def set_stream(self, stream):
        self.__stream = stream

    def set_academic_role(self, role):
        self.__academic_role = role

    # Methods
    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"academic_quals: {self.__academic_quals}"
        details += f"\n\t"
        details += f"stream: {self.__stream}"
        details += f"\n\t"
        details += f"academic_role: {self.__academic_role}"
        details += f"\n]"
        return details
