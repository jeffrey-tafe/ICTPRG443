import math


class Circle:
  def __init__(self, radius):
    self.__radius = radius

  def get_circumference(self):
    return (self.__radius * 2) * math.pi

  def get_area(self):
    return math.pi * (self.__radius ** 2)

  def get_radius(self):
    return self.__radius

  def __str__(self):
    return f"Radius: {self.__radius} , Area: {self.get_area()}, Circumference: {self.get_circumference()}"


