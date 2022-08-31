#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import openpyxl


def xlsx(file_location, sub_table, that_sok, column, distance):
    # 打开目标位置表格
    wb = openpyxl.load_workbook(file_location)
    # 定位分表
    ws = wb[sub_table]
    # 写入数据
    ws.cell(row=that_sok, column=column).value = distance
    wb.save(file_location)


if __name__ == '__main__':
    xlsx(file_location=r'/home/kylin/音乐/product_list.xlsx',
         sub_table='软件下载趋势', that_sok=5, column=1, distance='wang')
