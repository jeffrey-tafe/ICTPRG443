from Shape import Shape


class Square(Shape):

    # Constructor
    def __init__(self, name, length=0):
        self.__length = length
        super().__init__(name)

    # Getters
    def get_length(self):
        return self.__length

    # Setters
    def set_length(self, length):
        self.__length = length

    # Methods
    def area(self):
        return self.__length * self.__length

    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"name: {self.get_name()}"
        details += f"\n\t"
        details += f"length: {self.__length}"
        details += f"\n\t"
        details += f"area: {self.area()}"
        details += f"\n]"
        return details
