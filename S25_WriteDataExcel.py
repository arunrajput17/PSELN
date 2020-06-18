## Write data into Excel file

import openpyxl

path='D:\\Day Shift\\Zpyth\\Pseln\\TestFiles\\data25.xlsx'

workbook = openpyxl.load_workbook(path)

### Getting sheet from workbook method 1 (if only one sheet in excel)
sheet = workbook.active

# sheet = workbook.get_sheet_by_name('sheet1')        # by sheet name


# Writing data in sheet
for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value = 'welcome'        # writing in excel
        


workbook.save(path)     # Saving excel

