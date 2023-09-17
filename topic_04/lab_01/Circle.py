from Shape import Shape
import math


class Circle(Shape):

    # Constructor
    def __init__(self, name, radius):
        super().__init__(name)
        self.__radius = radius

    # Getters
    def get_radius(self):
        return self.__radius

    # Setters
    def set_radius(self, radius):
        self.__radius = radius

    # Methods
    def area(self):
        return (self.__radius * 2) * math.pi

    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"name: {self.get_name()}"
        details += f"\n\t"
        details += f"radius: {self.__radius}"
        details += f"\n\t"
        details += f"area: {self.area()}"
        details += f"\n]"
        return details
