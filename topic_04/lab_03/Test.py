from Vehicle import Vehicle

car1 = Vehicle("123abc", "Toyota", "Camry", 350)
car2 = Vehicle("987nbv", "Bugatti", "B80", 5000)
car3 = Vehicle("123abc", "Toyota", "Camry", 800)

print("\ncar1")
print(car1)

print("\ncar2")
print(car2)

print("\ncar3")
print(car3)

print("\nTesting comparing car1 to car2. Should be false")
print(car1.__eq__(car2))

print("\nTesting comparing car1 to car3. Should be true")
print(car1.__eq__(car3))
