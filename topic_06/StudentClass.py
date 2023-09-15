from TafePersonClass import TafePerson

class Student(TafePerson):
    def __init__(self, new_id = "id Not Set", new_first_name = "First Not Set", new_last_name = "Last Name Not Set",new_qual_code = "Qual Code Not Set"):
        super().__init__(new_id,new_first_name,new_last_name)
        self.__qual_code = new_qual_code

    def get_qual_code(self):
        return self.__qual_code

    def __str__(self):
        return f"{super().__str__()}, Qual Code: {self.__qual_code}"