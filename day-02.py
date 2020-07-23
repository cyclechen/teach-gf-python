# coding=utf-8

import xlrd

# 打开文件
data = xlrd.open_workbook('file/demo.xlsx')

# 查看工作表
data.sheet_names()
print("sheets：" + str(data.sheet_names()))

# 通过文件名获得工作表,获取工作表1
table = data.sheet_by_name('工作表1')

# 获取某个单元格的值，例如获取B3单元格值
cel_B3 = table.cell(3,2).value
print("第三行第二列的值：" + cel_B3)

#D列+5
cel_D2=table.cell(1,3).value+5
print("D2的正确年龄："+str(int(cel_D2)))