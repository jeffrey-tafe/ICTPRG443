class Shape:

    # Constructor
    def __init__(self, name):
        self.__name = name

    # Getters
    def get_name(self):
        return self.__name

    # Setters
    def set_name(self, name):
        self.__name = name

    # Methods
    def area(self):
        pass

    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"name: {self.__name}"
        details += f"\n]"
        return details
