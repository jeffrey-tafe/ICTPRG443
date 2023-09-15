cities_file = open("cities.txt","rt")
cities = cities_file.read()
cities_file.close()

cities_list = cities.splitlines()
cities_list.sort()

australian_cities = ["Adelaide","Darwin","Melbourne","Perth","Sydney"]

output = "City : Count"
australian_city_count = 0

for city in cities_list:
  if city not in output:
    output += f"\n{city} {cities_list.count(city)}"
    if city in australian_cities:
      australian_city_count += cities_list.count(city)


print(output)
print(f"\nTotal Australian City Instances: {australian_city_count}")