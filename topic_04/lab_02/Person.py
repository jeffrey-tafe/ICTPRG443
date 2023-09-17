class Person:

    # Constructor
    def __init__(self, name, tel_num, email, new_id):
        self.__name = name
        self.__tel_num = tel_num
        self.__email = email
        self.__id = new_id

    # Getters
    def get_name(self):
        return self.__name

    def get_tel_num(self):
        return self.__tel_num

    def get_email(self):
        return self.__email

    def get_id(self):
        return self.__id

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_tel_num(self, tel_num):
        self.__tel_num = tel_num

    def set_email(self, email):
        self.__email = email

    def set_id(self, new_id):
        self.__id = new_id

    # Methods
    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"name: {self.__name}"
        details += f"\n\t"
        details += f"tel_num: {self.__tel_num}"
        details += f"\n\t"
        details += f"email: {self.__email}"
        details += f"\n\t"
        details += f"id: {self.__id}"
        details += f"\n]"
        return details

    def __eq__(self, other):
        # using ID and name to determine equality
        return self.__id == other.__id and self.__name == other.__name
