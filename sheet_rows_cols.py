import xlrd
import xlwt
from xlwt import Workbook
wb = xlrd.open_workbook('write_test.xls')
sheet = wb.sheet_by_index(0)
print("Sheet rows: "+str(sheet.nrows))
print("Sheet cols: "+str(sheet.ncols))