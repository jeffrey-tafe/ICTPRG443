class Fan:

    # Constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Constructor
    def __init__(self, speed=SLOW, on=False, radius=0, color="blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # Getters
    def get_speed(self):
        return self.__speed

    def is_on(self):
        return self.__on

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    # Setters
    def set_speed(self, speed):
        self.__speed = speed

    def set_on(self, is_on):
        self.__on = is_on

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    # Methods
    def __str__(self):
        details = f"["
        details += f"\n\t"
        details += f"speed: {self.__speed}"
        details += f"\n\t"
        details += f"on: {self.__on}"
        details += f"\n\t"
        details += f"radius: {self.__radius}"
        details += f"\n\t"
        details += f"color: {self.__color}"
        details += f"\n]"
        return details
