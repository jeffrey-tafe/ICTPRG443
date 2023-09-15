class Bird:
  def __init__(self, new_weight=0, new_colour="black"):
    self.__weight = new_weight
    self.__colour = new_colour

  def draw(self):
    print("Drawing a Bird")
