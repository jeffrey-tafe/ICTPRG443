from Fan import Fan

print("\nTesting fan creation - fan1")
fan1 = Fan(Fan.FAST, True, 10, "yellow")
print(fan1)

print("\nTesting fan creation - fan1")
fan2 = Fan(Fan.MEDIUM, False, 5, "blue")
print(fan2)

print("\nTesting fan creation - fan3 (defaults)")
fan3 = Fan()
print(fan3)

print("\nTesting fan getters and setters")
fan3.set_on(True)
fan3.set_color("red")
fan3.set_speed(Fan.FAST)
fan3.set_radius(12)

print(f"Fan3 On: {fan3.is_on()}")
print(f"Fan3 Color: {fan3.get_color()}")
print(f"Fan3 Speed: {fan3.get_speed()}")
print(f"Fan3 Radius: {fan3.get_radius()}")
