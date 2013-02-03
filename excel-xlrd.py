# Demonstrates basic xlrd functions for working with Excel files
# (Excel 97-2003)

import xlrd

wb = xlrd.open_workbook('excel-xlrd-sample.xls')

# Print the sheet names
print wb.sheet_names()

# Get the first sheet either by index or by name
sh = wb.sheet_by_index(0)

# Iterate through rows, returning each as a list that you can index:
for rownum in range(sh.nrows):
    print sh.row_values(rownum)

# If you just want the first column:
first_column = sh.col_values(0)
print first_column

# Index individual cells:
cell_c4 = sh.cell(3, 2).value
# Or you can use:
#cell_c4 = sh.cell(rowx=3, colx=2).value
print cell_c4

# Let's say you want the same cell from x identical sheets in a workbook:
x = 2
while x >= 0:
    sh = wb.sheet_by_index(x)
    cell_x = sh.cell(2, 3).value
    print cell_x
    x = x - 1
