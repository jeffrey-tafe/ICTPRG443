import math

class Circle:
  def __init__(self, new_radius):


    self.set_radius(new_radius)
    self.set_circumference()
    self.set_area()

  def set_radius(self, new_radius):
    self.__radius = new_radius

  def set_circumference(self):
    self.__circumference = 2 * math.pi * self.__radius

  def set_area(self):
    self.__area = math.pi * (self.__radius ** 2)

  def get_radius(self):
    return self.__radius

  def get_circumference(self):
    return self.__circumference

  def get_area(self):
    return self.__area

  def print_circle(self):
    print(f"\nRadius: {self.__radius}\nCircumference: {self.__circumference}\nArea: {self.__area}")
