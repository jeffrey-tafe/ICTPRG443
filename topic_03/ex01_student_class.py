class Student:
  def __init__(self, new_id = "NO ID SET", new_name = "NO NAME SET", new_email = "NO EMAIL SET"):   #dunder method
    self.set_id(new_id)
    self.set_name(new_name)
    self.set_email(new_email)

  def get_id(self):
    return self.__id

  def get_name(self):
    return self.__name

  def get_email(self):
    return self.__email

  def set_id(self, new_id):
    if new_id.strip() != "":
      self.__id = new_id
    else:
      print("Error: ID cannot be set to blank")
      self.__name = "NO ID SET"

  def set_name(self, new_name):
    if new_name.strip() != "":
      self.__name = new_name.strip()
    else:
      print("Error: Name cannot be set to blank")
      self.__name = "NO NAME SET"

  def set_email(self, new_email):
    if new_email.strip() != "":
      self.__email = new_email.strip()
    else:
      print("Error: Email cannot be set to blank")
      self.__email = "NO NAME SET"

  def __display_details(self):
    return f"\nID: {self.__id}\nName: {self.__name}\nEmail: {self.__email}"

  def __str__(self):
    return self.__display_details()