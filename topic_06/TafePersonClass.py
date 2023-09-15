class TafePerson:

  def __init__(self, new_id="ID Not Set", new_first_name="First Name Not Set", new_last_name="Last Name Not Set"):
    self.__id = new_id
    self.__first_name = new_first_name
    self.__last_name = new_last_name

  def get_id(self):
    return self.__id

  def get_first_name(self):
    return self.__first_name

  def get_last_name(self):
    return self.__last_name

  def __str__(self):
    return f"ID: {self.__id}, First Name: {self.__first_name}, Last Name: {self.__last_name}"


