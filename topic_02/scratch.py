import csv

products = []
with open("products.txt", "rt") as data:
  for line in csv.reader(data, delimiter=";"):
    product = {
      "ID": line[0],
      "Product": line[1],
      "Price": float(line[2])
    }
    products.append(product)

print(products)