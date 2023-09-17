from Person import Person


class Staff(Person):
    # Constructor
    def __init__(self,
                 name,
                 tel_num,
                 email,
                 new_id,
                 emp_type,
                 dept,
                 salary):
        super().__init__(name, tel_num, email, new_id)
        self.__emp_type = emp_type
        self.__dept = dept
        self.__salary = salary

    # Getters
    def get_emp_type(self):
        return self.__emp_type

    def get_dept(self):
        return self.__dept

    def get_salary(self):
        return self.__salary

    # Setters
    def set_emp_type(self, emp_type):
        self.__emp_type = emp_type

    def set_dept(self, dept):
        self.__dept = dept

    def set_salary(self, salary):
        self.__salary = salary

    # Methods
    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"emp_type: {self.__emp_type}"
        details += f"\n\t"
        details += f"dept: {self.__dept}"
        details += f"\n\t"
        details += f"salary: {self.__salary}"
        details += f"\n]"
        return details
