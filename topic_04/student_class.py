class Student:

  def __init__(self, new_name, new_address):
    self.__name = new_name
    self.__address = new_address

  def __str__(self):
    return f"Name: {self.__name}, Address: {self.__address}"