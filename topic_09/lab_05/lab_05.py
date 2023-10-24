from product import Product
from openpyxl import Workbook
import os
import random

# Delete existing result workbook if exists
result_workbook_path = "result.xlsx"
if os.path.exists(result_workbook_path):
    os.remove(result_workbook_path)

# Create python objects and add to list
products = []
for _ in range(0, 5):
    product = Product(
        random.randint(100, 999),
        random.randint(100, 999),
        f"Product {random.randint(100, 999)}",
        f"Cat{random.randint(100, 999)}"
    )
    products.append(product)

# Create workbook and active sheet
workbook = Workbook()
sheet = workbook.active

# Append headers to worksheet
headers = ("ID", "Parent", "Title", "Category")
sheet.append(headers)

# Loop through products to set values in workbook
for product in products:
    sheet.append((product.id, product.parent, product.title, product.category))

workbook.save("result.xlsx")
