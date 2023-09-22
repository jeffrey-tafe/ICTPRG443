class Person:

    # Constructor
    def __init__(self, new_id, first_name, last_name):
        self.__id = new_id
        self.__first_name = first_name
        self.__last_name = last_name

    # Getters
    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    # To string override
    def __str__(self):
        details = f"\n" + super().__str__()
        details += f"\n["
        details += f"\n\tID: {self.__id}"
        details += f"\n\tFirst Name: {self.__first_name}"
        details += f"\n\tLast Name: {self.__last_name}"
        details += f"\n]"
        return details


# Exmaple instantiation
# person = Person("test","Jeffrey", "Smith")
# print(person)

