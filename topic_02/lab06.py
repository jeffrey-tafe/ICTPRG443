import csv

# Get customers and convert each row to dictionary in a list
customers = []
with open("customers.txt", "rt") as data:
  for line in csv.reader(data, delimiter=" "):
    customer = {
      "ID": line[0],
      "Name": f"{line[1]} {line[2]}",
      "Contact Number": line[3]
    }
    customers.append(customer)


# Get sales and convert each row to dictionary in a list
sales = []
with open("sales.txt", "rt") as data:
  for line in csv.reader(data, delimiter=" "):
    sale = {
      "Customer": line[0],
      "Product": line[1],
      "Quantity": int(line[2])
    }
    sales.append(sale)


# Get products and convert each row to dictionary in a list
products = []
with open("products.txt", "rt") as data:
  for line in csv.reader(data, delimiter=";"):
    product = {
      "ID": line[0],
      "Name": line[1],
      "Price": float(line[2])
    }
    products.append(product)


# Helper function to retrieve a dict record from a list
def get_record_from_list(target_list, key, value):
  for item in target_list:
    if item[key] == value:
      return item
  return None

# Build sales report
print("Customer Name | Product Name | Total Spent")
for sale in sales:
  customer = get_record_from_list(customers, "ID", sale["Customer"])
  product = get_record_from_list(products, "ID", sale["Product"])
  total = product["Price"] * sale["Quantity"]

  print(f"{customer['Name']} | {product['Name']} | {total}")


  # print(sale["Quantity"])

  # total = product["Price"] * sale["Quantity"]

  # print(f"{customer['Name']} | {product['Name']} | {total}")




