class Vehicle:
    # Constructor
    def __init__(self,
                 registration_number="NOT REGISTERED",
                 make="NO MAKE",
                 model="NO MODEL",
                 engine_capacity="NO CAPACITY"
                 ):
        self.__registration_number = registration_number
        self.__make = make
        self.__model = model
        self.__engine_capacity = engine_capacity

    # Getters
    def get_registration_number(self):
        return self.__registration_number

    def get_make(self):
        return self.__make

    def get_engine_capacity(self):
        return self.__engine_capacity

    def get_model(self):
        return self.__model

    # Setters
    def set_registration_number(self, number):
        self.__registration_number = number

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity

    # Methods
    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"registration_number: {self.__registration_number}"
        details += f"\n\t"
        details += f"make: {self.__make}"
        details += f"\n\t"
        details += f"model: {self.__model}"
        details += f"\n\t"
        details += f"engine_capacity: {self.__engine_capacity}"
        details += f"\n]"
        return details

    def __eq__(self, other):
        print("This Object")
        print(self)
        print("Other Object")
        print(other)
        return self.__registration_number == other.get_registration_number() and \
            self.__make == other.get_make() and \
            self.__model == other.get_model()
