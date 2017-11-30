import xlrd, xlwt

rb = xlrd.open_workbook('/home/mj/ip.xlsm')
sheet = rb.sheet_by_index(0)
val = [sheet.row_values(rownum)[0] for rownum in range(sheet.nrows)]
for i in val:
    print(i)

