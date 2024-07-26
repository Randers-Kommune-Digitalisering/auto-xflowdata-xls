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


def write_to_workbook(filename, data: list):

    # Check if filename is valid and data is a list
    if filename is False or not isinstance(data, list):
        return False

    # Open workbook
    workbook = openpyxl.load_workbook(filename)

    # Set initial worksheet id
    worksheet_id = 0

    # Loop through all the dicts in data
    for item in data:

        # Check if respective worksheet exists
        if not workbook.worksheets[worksheet_id]:
            print(f'Worksheet with id {worksheet_id} not found')
            break

        # Select the worksheet to edit
        worksheet = workbook.worksheets[worksheet_id]

        # Write data to cells
        for key in item:
            worksheet[key] = item[key]

        # Increment the worksheet id
        worksheet_id += 1

    # Save the workbook
    workbook.save(filename)
    workbook.close()

    return True


# Test functions

if os.path.exists('demo.xlsx'):
    print( write_to_workbook(create_workbook(), [{'A1': 'Hi', 'A2': 'there'}]) )

else:
    print('File not found')
