# def jie_cheng(n):
#     if n <= 1:
#         return 1
#     print(n * jie_cheng(n-1))
#     return n * jie_cheng(n - 1)
#
#
# print(jie_cheng(5))
from pprint import pprint
import xlrd
import openpyxl
import json
import os.path
import random
from pymysql import cursors
import pymysql
import pandas as pd
import numpy as np
import time
import turtle

# 查重插入
cait = {'id': ['A', 'B', 'A', 'C']}
li = [1, 2, 3, 3, 4, 2, 3, 4, 5, 6]
lii = [1, 7, 8, 9, 10, 11]
data = pd.DataFrame(cait)
c = data.drop_duplicates(['id'])
print("3", c)
a = np.unique(li)
print("2", a)

# """excle的操作"""
#
# class ExcleHeandle:
#     def __init__(self, fpath):
#         self.fpath = fpath
#
#     def read(self, sheet_name):
#         wb = openpyxl.open(self.fpath)
#         # print(wb)
#         ws = wb[sheet_name]
#         data = list(ws.values)
#         key = data[0]
#         all_data = []
#         for val in data[1:]:
#             new_data = dict(zip(key, val))
#             all_data.append(new_data)
#         return all_data
#
#     def write(self, sheet_name, row, colum, date):
#         wb = openpyxl.open(self.fpath)
#         # print(wb)
#         ws = wb[sheet_name]
#         ws.cell(row=row, column=colum).value = date
#         wb.save(self.fpath)
#         wb.close()
#
#
# if __name__ == '__main__':
#     file = ExcleHeandle("asd.xlsx")
#     data = file.read('Sheet1')
#     pprint(data)

a = random.uniform(1, 10)
a = round(a, 2)
print(a)
# 倒计时
from colorama import init, Fore
from zhdate import ZhDate
import datetime


def get_week_day(date):
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]


def time_parse(today):
    distance_year = (datetime.datetime.strptime(f"{today.year}-01-01", "%Y-%m-%d").date() - today).days
    distance_year = distance_year if distance_year > 0 else (
            datetime.datetime.strptime(f"{today.year + 1}-01-01", "%Y-%m-%d").date() - today).days

    distance_big_year = (ZhDate(today.year, 1, 1).to_datetime().date() - today).days
    distance_big_year = distance_big_year if distance_big_year > 0 else (
            ZhDate(today.year + 1, 1, 1).to_datetime().date() - today).days

    distance_4_5 = (datetime.datetime.strptime(f"{today.year}-04-05", "%Y-%m-%d").date() - today).days
    distance_4_5 = distance_4_5 if distance_4_5 > 0 else (
            datetime.datetime.strptime(f"{today.year + 1}-04-05", "%Y-%m-%d").date() - today).days

    distance_5_1 = (datetime.datetime.strptime(f"{today.year}-05-01", "%Y-%m-%d").date() - today).days
    distance_5_1 = distance_5_1 if distance_5_1 > 0 else (
            datetime.datetime.strptime(f"{today.year + 1}-05-01", "%Y-%m-%d").date() - today).days

    distance_5_5 = (ZhDate(today.year, 5, 5).to_datetime().date() - today).days
    distance_5_5 = distance_5_5 if distance_5_5 > 0 else (
            ZhDate(today.year + 1, 5, 5).to_datetime().date() - today).days

    distance_8_15 = (ZhDate(today.year, 8, 15).to_datetime().date() - today).days
    distance_8_15 = distance_8_15 if distance_8_15 > 0 else (
            ZhDate(today.year + 1, 8, 15).to_datetime().date() - today).days

    distance_10_1 = (datetime.datetime.strptime(f"{today.year}-10-01", "%Y-%m-%d").date() - today).days
    distance_10_1 = distance_10_1 if distance_10_1 > 0 else (
            datetime.datetime.strptime(f"{today.year + 1}-10-01", "%Y-%m-%d").date() - today).days

    # print("距离周末: ", 5 - today.weekday())
    # print("距离元旦: ", distance_year)
    # print("距离大年: ", distance_big_year)
    # print("距离清明: ", distance_4_5)
    # print("距离劳动: ", distance_5_1)
    # print("距离端午: ", distance_5_5)
    # print("距离中秋: ", distance_8_15)
    # print("距离国庆: ", distance_10_1)

    time_ = [
        {"v_": 5 - 1 - today.weekday(), "title": "周末"},  # 距离周末
        {"v_": distance_year, "title": "元旦"},  # 距离元旦
        {"v_": distance_big_year, "title": "过年"},  # 距离过年
        {"v_": distance_4_5, "title": "清明节"},  # 距离清明
        {"v_": distance_5_1, "title": "劳动节"},  # 距离劳动
        {"v_": distance_5_5, "title": "端午节"},  # 距离端午
        {"v_": distance_8_15, "title": "中秋节"},  # 距离中秋
        {"v_": distance_10_1, "title": "国庆节"},  # 距离国庆
    ]

    time_ = sorted(time_, key=lambda x: x['v_'], reverse=False)
    return time_


def countdown():
    init(autoreset=True)
    today = datetime.date.today()
    now_ = f"{today.year}年{today.month}月{today.day}日"
    week_day_ = get_week_day(today)
    print(f'\n\t\t {Fore.GREEN}{now_} {week_day_}')

    str_ = '''
         开始!
    '''
    print(f'{Fore.RED}{str_}')

    time_ = time_parse(today)
    for t_ in time_:
        print(f'\t\t {Fore.RED}距离{t_.get("title")}还有: {t_.get("v_")+1}天')
    tips_ = '''
         结束!
    '''
    print(f'{Fore.RED}{tips_}')



if __name__ == '__main__':
    countdown()
