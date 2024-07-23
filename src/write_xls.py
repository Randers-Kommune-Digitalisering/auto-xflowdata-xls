import openpyxl
import time
import shutil
import os

def create_workbook():
    # Create filename using timestamp
    filename = time.strftime("%Y%m%d-%H%M%S") + ".xlsx"

    # Copy the template file
    shutil.copy2("demo.xlsx", filename)
    
    # Check if the file was copied successfully
    if os.path.exists(filename):
        return filename

    return False

def write_to_file(filename):
    if filename == False:
        return False

    # Open workbook
    workbook = openpyxl.load_workbook(filename)
    
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


# Test functions

if os.path.exists("demo.xlsx"):
    write_to_file(create_workbook())

else:
    print("File not found")