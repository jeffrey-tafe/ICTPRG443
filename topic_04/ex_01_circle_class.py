from ex_01_shape_class import Shape

class Circle(Shape):
  def __init__(self, new_x=0, new_y=0, new_colour='black', new_radius=5):
    super().__init__(new_x, new_y, new_colour)
    self.__radius = new_radius

  def get_radius(self):
    return self.__radius

  def __str__(self):
    return f"{super().__str__()} \nradius: {self.__radius}"

  def __eq__(self, other):
    return super().__eq__(other) and self.__radius == other.__radius

  def draw(self):
    print("Drawing a Circle")
