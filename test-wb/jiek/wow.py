import logging

import pymysql
import pandas as pd
from pymysql import cursors

global cur_data


def inset_user():
    """造数据"""
    import random
    user = ''
    user1 = ['周', '赵', '钱', '孙', '李', '朱', '吴', '郑', '王', '张', '谢', '麦', '冯', '刘', '汤', '熊']
    user2 = ['春', '兰', '怀', '雅', '琪', '安', '子', '发', '若', '正', '耀', '让', '俊', '要', '梓', '浩']
    user3 = ['玉', '建', '嚄', '宇', '玲', '满', '曼', '末', '旺', '卫', '才', '伟', '从', '峰', '费', '坤']
    user1 = random.choice(user1)[0]
    user += user1
    user2 = random.choice(user2)[0]
    user += user2
    user3 = random.choice(user3)[0]
    user += user3
    sex = [1, 2]
    age = random.randint(18, 40)
    teacher = random.choice(sex)
    psd = ''
    gradr = ['一年级', '二年级', '三年级', '四年级', '五年级', '六年级', '七年级', '八年级', '九年级']
    gradr = random.choice(gradr)
    for i in range(6):
        num = str(random.randint(0, 9))
        psd += num

    student = ''
    for i in range(6):
        mu = str(random.randint(0, 9))
        student += mu
    # DB_SQL().insert_news(user, psd,gradr,age,teacher, student)


class DB_SQL(object):
    def __init__(self):
        """初始化"""
        self.host = "rm-wz922iub1i0q7eylppo.mysql.rds.aliyuncs.com"
        self.username = "jiangan"
        self.password = "Jiangan2021"
        self.db_name = "benben_league"

        self.connect = pymysql.connect(host=self.host,
                                       password=self.password,
                                       user=self.username,
                                       db=self.db_name,
                                       charset='utf8',
                                       cursorclass=cursors.DictCursor)
        self.cursor = self.connect.cursor()

    def login_add(self, user):
        """登录"""
        try:
            self.cursor.execute("select * from member_user where account = {};".format(user))
            cur_data = self.cursor.fetchall()
            sql_data = cur_data[0]
            print("校验成功")
            print(sql_data)
        except Exception as e:
            print("FILL", e)

        finally:
            self.cursor.close()
            self.connect.close()


qa = DB_SQL()


dict_a = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
          'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, ',X': 24, 'Y': 25,
          'Z': 26}
a = input()
b = input()
s1 = 1
s2 = 1
for i in range(0, len(a)):
    c = ord(a[i]) - 64
    s1 = s1 * c
for j in range(0, len(b)):
    d = ord(b[j]) - 64
    s2 = s2 * d
if s1 % 47 == s2 % 47:
    print('GO')
else:
    print('STAY')
