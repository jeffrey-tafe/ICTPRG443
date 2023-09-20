class Alien:

    __valid_alien_types = ["Martian", "Venusian", "Plutonian", "Neptunian"]

    def __init__(self, strength = 0, lives = 0, alien_type = "Alien Type Not Set"):
        self.__strength = strength
        self.__lives = lives
        self.set_alien_type(alien_type)

    def set_strength(self, strength):
        self.__strength = strength

    def set_lives(self, lives):
        self.__lives = lives

    def set_alien_type(self, new_alien_type):
        if new_alien_type in Alien.__valid_alien_types:
            self.__alien_type = new_alien_type.strip()
        else:
            self.__alien_type = "Alien Type Not Set"

    def get_alien_type(self):
        return self.__alien_type

    def get_strength(self):
        return self.__strength

    def get_lives(self):
        return self.__lives

    def __str__(self):
        return f"\tStrength: {self.get_strength()}\n\tLives: {self.get_lives()}"
