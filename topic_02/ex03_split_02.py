product_file = open("products.txt", "rt")

for line in product_file:
  product_id, product_name, product_cost = line.split(" ")
  print(f"\nProduct ID: {product_id}\nProduct Name: {product_name}\nProduct Cost: {float(product_cost):0.02f}")