import openpyxl
from product import Product


FILE_NAME = 'products.xlsx'

PROD_ID_COL = 3
PROD_PARENT_COL = 4
PROD_TITLE_COL = 5
PROD_CATEGORY = 6

my_workbook = openpyxl.load_workbook(FILE_NAME, read_only=True)
active_sheet = my_workbook["Reviews"]
products = []

for row in active_sheet.iter_rows(min_row=2, values_only=True):
    product = Product(
        id=row[PROD_ID_COL],
        parent=str(row[PROD_PARENT_COL]),
        title=row[PROD_TITLE_COL],
        category=row[PROD_CATEGORY]
    )
    products.append(product)

for product in products:
    print(f"{product.id}\t{product.parent}\t{product.category}\t{product.title}")
