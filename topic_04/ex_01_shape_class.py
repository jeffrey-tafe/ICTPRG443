from abc import ABC,abstractmethod

class Shape(ABC):
  def __init__(self, new_x_pos=0, new_y_pos=0, new_colour="black"):
    self.__x_pos = new_x_pos;
    self.__y_pos = new_y_pos;
    self.__colour = new_colour;

  @abstractmethod
  def draw(self):
    print("Drawing a Shape")

  def get_x_pos(self):
    pass

  def get_y_pos(self):
    pass

  def get_colour(self):
    pass

  def move(self):
    print("Move shape")

  def erase(self):
    pass

  def __str__(self):
    return f"x Position: {self.__x_pos}\ny Position: {self.__y_pos}\ncolour: {self.__colour}"

  def __eq__(self, other):
    return ((self.__x_pos == other.__x_pos) and
            (self.__y_pos == other.__y_pos) and
            (self.__colour == other.__colour)
            )
