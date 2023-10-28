# Sets Lab 01

class Food:

    # Constants
    __DEF_NAME = "NAME NOT SET"
    __DEF_COOKING_METHOD = "COOKING METHOD NOT SET"

    # Constructor
    def __init__(self, name = __DEF_NAME, cooking_method = __DEF_COOKING_METHOD):
        self.__name = name
        self.__cooking_method = cooking_method

    # Methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_cooking_method(self):
        return self.__cooking_method

    def set_cooking_method(self, cooking_method):
        self.__cooking_method = cooking_method

    def __str__(self):
        details = f"\n["
        details += f"\n\tName: {self.__name}"
        details += f"\n\tCooking Method: {self.__cooking_method}"
        details += f"\n]"
        return details

    def __eq__(self, other):
        return (self.get_name() == other.get_name() and
                self.get_cooking_method() == other.get_cooking_method())

    def __hash__(self):
        return hash((self.__name, self.__cooking_method))