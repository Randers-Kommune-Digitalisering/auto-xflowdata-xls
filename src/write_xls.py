import openpyxl
import time

def write_to_file():
    # Open workbook
    workbook = openpyxl.load_workbook("demo.xlsx")
    
    # Select the first sheet
    worksheet = workbook.active

    # Assigned data directly to cells
    worksheet['A1'] = "Hi"

    # Read the cell value
    row_number = 0
    column_number = 0
    cell_value = worksheet.cell(row=row_number + 1, column=column_number + 1).value
    print(cell_value)
    
    # Save the workbook
    workbook.close()

write_to_file()