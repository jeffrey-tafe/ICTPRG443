from ex_01_shape_class import Shape
from ex_01_circle_class import Circle
from ex_01_bird_class import Bird

def draw_shape(shape):
  shape.draw()


def main():
  # shape1 = Shape()
  # shape2 = Shape(10, 20, "yellow")

  # print(f"\nshape1\n{shape1}")
  # print(f"\nshape2\n{shape2}")

  circle1 = Circle()
  circle2 = Circle(0, 0, "black", 5)

  print(f"\ncircle1\n{circle1}")
  print(f"\ncircle2\n{circle2}")

  print(circle1.__eq__(circle1))
  print(circle1.__eq__(circle2))

  draw_shape(circle1)
  # draw_shape(shape2)

  bird1 = Bird(2, "white")
  draw_shape(bird1)

  circle1.move()

main()

