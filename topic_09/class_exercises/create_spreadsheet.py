import openpyxl
from openpyxl.styles import Font

# Create a new workbook
my_workbook = openpyxl.Workbook()

active_sheet = my_workbook.active

active_sheet['A1'] = "Hello"
active_sheet['B1'] = "World"
active_sheet.title = "Hello_Sheet"

new_sheet_name = "World_Sheet"
my_workbook.create_sheet(new_sheet_name)
active_sheet = my_workbook[new_sheet_name]

active_sheet['A1'] = "Welcome"
active_sheet['B1'] = "to"
active_sheet['C1'] = "Adelaide"
active_sheet.title = new_sheet_name

active_sheet = my_workbook["Hello_Sheet"]
active_sheet['A3'] = "Switched back"

active_sheet.sheet_properties.TabColor = "FFFF00"
active_sheet['A3'].font = Font(bold=True)
active_sheet['B1'].font = Font(bold=True, italic=True, underline='double')

active_sheet.column_dimensions['A'].width = 50
active_sheet.row_dimensions[1].height = 30


active_sheet['E1'] = 1
active_sheet['E2'] = 2
active_sheet['E3'] = 3
active_sheet['E4'] = 4
active_sheet['E5'] = 5

total = 0

cell_range = 'E2:E5'

for row in active_sheet[cell_range]:
    for cell in row:
        total += cell.value

active_sheet['D6'] = "TOTAL"
active_sheet['E6'] = total

try:
    my_workbook.save(filename="hello_world.xlsx")
    print("Workbook saved")
except PermissionError:

    print("Error: Cannot save file at this time, file may be in use")
except Exception as ex:
    print(f"{type(ex).__name__, ex.args}")
