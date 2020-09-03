# -*- coding: utf-8 -*-
import xlrd
import xlwt
#from datetime import date, datetime

file= "C:/Users/Administrator/Desktop/赵哲师姐/"  #默认文件路径

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(file+"白玉杰数据处理.xlsx")
    sheet1 = workbook.sheet_by_name('Sheet1')  #打开名叫Sheet1的excel

    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    cols = sheet1.col_values(0)  #读取第0列
    flags =sheet1.col_values(1)  #读取第1列
    print(cols)
    print(flags)
def write_excel():

    book = xlwt.Workbook() #新建一个excel
    sheet = book.add_sheet('汇总处理') #添加一个sheet页
    sheet.write(0,0,'姓名') #Excel第一行第一列写入姓名
    sheet.write(0,1,'性别') #Excel第一行第二列写入性别
    sheet.write(0,2,'年龄') #Excel第一行第三列写入年龄
    book.save(file+"白玉杰数据处理后.xls") #微软的office不能用xlsx结尾的，wps随意
    print("数据写入成功")
def mydeal_excel():
    workbook = xlrd.open_workbook(file + "白玉杰数据处理.xlsx")
    sheet1 = workbook.sheet_by_name('Sheet1')  # 打开名叫Sheet1的excel
    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    jutitime = sheet1.col_values(2)  # 读取具体相差时间
    chaday = sheet1.col_values(3)    # 读取相差时间
    type = sheet1.col_values(4)      # 读取投诉类型
    taidu =sheet1.col_values(5)      #读取态度
    place =sheet1.col_values(6)      #签收部门

    book = xlwt.Workbook() #新建一个excel
    sheet = book.add_sheet('汇总处理原') #添加一个sheet页
    sheet2 =book.add_sheet("按照序号")
    sheet.write(0,0,'姓名') #Excel第一行第一列写入姓名
    sheet.write(0,1,'性别') #Excel第一行第二列写入性别
    sheet.write(0,2,'年龄') #Excel第一行第三列写入年龄
    book.save("白玉杰数据处理后.xls") #微软的office不能用xlsx结尾的，wps随意
    print("数据写入成功")
def countplace():
    workbook = xlrd.open_workbook(file + "白玉杰数据处理.xlsx")
    sheet1 = workbook.sheet_by_name('Sheet1')  # 打开名叫Sheet1的excel
    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    words = sheet1.col_values(6)  # 读取第0列
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(str(len(items)))
    book = xlwt.Workbook()  # 新建一个excel
    sheet = book.add_sheet('部门统计')  # 添加一个sheet页
    # sheet.write(0, 1, '部门')  # Excel第一行第一列写入部门
    # sheet.write(1, 2, '个数')  # Excel第一行第二列写入个数
    for i in range(len(items)):
        print("我是："+str(items[i]))
        word, count = items[i]
        sheet.write(i, 1, word)  # Excel第一行第一列写入姓名
        sheet.write(i, 2, count)  # Excel第一行第二列写入性别

        print("{0:<10}{1:>5}".format(word, count))
    book.save(file + "白玉杰数据处理后.xls")  # 微软的office不能用xlsx结尾的，wps随意
    print("数据写入成功")


if __name__ == '__main__':
    # read_excel()
    # write_excel()
    #mydeal_excel()
    countplace()