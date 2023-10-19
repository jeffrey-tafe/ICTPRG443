import openpyxl
from openpyxl.chart import BarChart3D, Reference
from openpyxl.chart.label import DataLabelList


my_workbook = openpyxl.Workbook()
active_sheet = my_workbook.active
active_sheet.title = "Products"

rows = [
    ["Products", "Online", "Store"],
    [1, 30, 45],
    [2, 40, 30],
    [3, 40, 25],
    [4, 50, 30],
    [5, 30, 25],
    [6, 25, 35],
]

for row in rows:
    if row[0] != 'Product':
        prod_value = "Product " + str(row[0])
    else:
        prod_value = row[0]
    active_sheet.append([prod_value, row[1], row[2]])


my_chart = BarChart3D()
data = Reference(worksheet=active_sheet, min_row=1, max_row=7, min_col=2, max_col=3)

my_chart.add_data(data, titles_from_data=True)
active_sheet.add_chart(my_chart, "F7")

categories = Reference(active_sheet, min_col=1, min_row=1, max_row=7)
my_chart.set_categories(categories)

my_chart.title = "Products By Store"

data_labels = DataLabelList()
data_labels.showVal = True
my_chart.dataLabels = data_labels

my_workbook.save('product_bar_chart.xlsx')
