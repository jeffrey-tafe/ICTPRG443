from address_class import Address

class Lecturer:

  def __init__(self, new_name, new_street, new_suburb, new_postcode):
    self.__name = new_name
    self.__address = Address(new_street,new_suburb,new_postcode)

  def __str__(self):
    return f"Name: {self.__name}, Address: {self.__address}"
