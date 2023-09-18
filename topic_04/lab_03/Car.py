from Vehicle import Vehicle

class Car(Vehicle):
    # Constructor
    def __init__(self,
                 registration_number="NOT REGISTERED",
                 make="NO MAKE",
                 model="NO MODEL",
                 engine_capacity="NO CAPACITY",
                 body_type="NO BODY TYPE",
                 is_automatic=False
                 ):
        super().__init__(
            registration_number,
            make,
            model,
            engine_capacity
        )
        self.__body_type = None
        self.set_body_type(body_type)
        self.__is_automatic = is_automatic

    # Getters
    def get_body_type(self):
        return self.__body_type

    def is_automatic(self):
        return self.__is_automatic

    # Setters
    def set_body_type(self, body_type):
        body_types = ["sedan", "sports", "coupe"]
        if body_type.lower() in body_types:
            self.__body_type = body_type.lower()
        else:
            self.__body_type = "NO BODY TYPE"

    def set_is_automatic(self, is_automatic):
        self.__is_automatic = is_automatic

    # Methods
    def __str__(self):
        details = super().__str__()
        details += f"\n["
        details += f"\n\t"
        details += f"body_type: {self.__body_type}"
        details += f"\n\t"
        details += f"is_automatic: {self.__is_automatic}"
        details += f"\n]"
        return details
