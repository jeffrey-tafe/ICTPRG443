class Employee:
    # Constructor
    def __init__(self,
                 employee_id="NO ID",
                 full_name="NO NAME",
                 email="NO EMAIL",
                 tel_num="NO TEL NUM"):
        self.__employee_id = employee_id
        self.__full_name = full_name
        self.__email = email
        self.__tel_num = tel_num

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, value):
        self.__employee_id = value

    def get_full_name(self):
        return self.__full_name

    def set_full_name(self, value):
        self.__full_name = value

    def get_email(self):
        return self.__email

    def set_email(self, value):
        self.__email = value

    def get_tel_num(self):
        return self.__tel_num

    def set_tel_num(self, value):
        self.__tel_num = value

    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"employee_id: {self.__employee_id}"
        details += f"\n\t"
        details += f"full_name: {self.__full_name}"
        details += f"\n\t"
        details += f"email: {self.__email}"
        details += f"\n\t"
        details += f"tel_num: {self.__tel_num}"
        details += f"\n]"
        return details
