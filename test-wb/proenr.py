import logging
import random


def random_phone():
    """随机获取手机号"""
    reu = ""
    reu1 = "1"
    cat_phone = ["32", "58", "31", "71", "55", "33", "47"]
    reu = reu + reu1
    cat_phone = random.choices(cat_phone)[0]
    reu = reu + cat_phone
    for i in range(8):
        num = str(random.randint(1, 9))
        reu += num
    return reu


def print_menu():
    """打印提示菜单信息"""
    print("=" * 25)
    print("\t~新款扣扣~")
    print("\t1: 注册")
    print("\t2: 登录")
    # print("\t2:删除学生信息")
    # print("\t3:修改学生信息")
    # print("\t4:查找学生信息")
    # print("\t5:显示学生信息")
    print("\t6: 退出")
    print("=" * 25)


class StudentSys(object):
    def __init__(self):
        # 实例属性
        self.student = {}
        self.names = []

        self.info = "1:注册|2:删除|3:修改|4:查找|5:显示|6:退出系统|7：登录|0：清空系统"

    # 打印提示信息(菜单)

    def login(self):
        name = input("输入账号：")
        psd = input("输入密码： ")
        for names in self.names:

            if name == names["name"] and psd == names["psd"]:
                print("登录成功:{}".format(name))
                break
            elif name != names["name"] or psd != names["psd"]:
                print("用户名或密码错误")
                return self.login()

    def add_info(self):
        """添加信息"""
        name = input("注册用户名:")
        if len(name) < 6:
            print("用户名长度不能小于6")
            return self.add_info()
        phone = input("请添加手机号(不填为随机):")
        if phone == "":
            phone = random_phone()
        elif len(phone) > 11:
            phone = random_phone()
        psd = input("请输入密码:")
        if len(psd) < 6:
            print("密码长度不能小于6位")
            return self.add_info()
        elif psd == '123456' or psd == '123123':
            print("密码过于简单，请重新输入")
            return self.add_info()
        self.student["name"] = name
        self.student["phone"] = phone
        self.student["psd"] = psd

        for names in self.names:
            if name == names["name"]:
                print("用户名重复，请重新输入")
                return self.add_info()
            elif psd == name:
                print("用户名不能和密码一样")
                return self.add_info()

        self.names.append(self.student)
        print(self.names)
        self.show_info()
        self.save_info()

    def delete_info(self):
        """删除信息"""
        # 根据下标删除和内容删除和末尾删除
        del_name = input("请输入删除的用户名:")
        for name in self.names:
            # name:{"name":"曹操"....}
            if del_name == name.get("name"):
                self.names.remove(name)

        self.show_info()
        self.save_info()

    def modify_info(self):
        """修改信息"""
        # 根据下标修改index是列表的方法
        find_name = input("请输入您需要的用户名: ")
        flag = 0  # 0,没有找到,1找到了
        for name in self.names:

            if find_name == name["name"]:
                new_name = input("请输入新的名字: ")
                new_psd = input("请输入新的密码")
                new_phone = input("请输入新的手机号")

                if len(new_name) < 6:
                    print("用户名长度不能小于6位")
                    self.new_modify()
                name["name"] = new_name
                if len(new_psd) < 6:
                    print("密码长度不能小于5位")

                if new_phone == '':
                    pass

                flag = 1
                break

        if flag == 0:
            print("该名用户%s不存在" % find_name)
            self.modify_info()

        else:
            self.show_info()
        self.save_info()

    def new_modify(self):
        """确认修改信息"""
        new_name = input("请重新输入新的用户名： ")
        for name in self.names:
            if len(new_name) < 6:
                print("用户名长度不能小于6位")
                self.new_modify()
            name["name"] = new_name
        else:
            self.show_info()
        self.save_info()

    def find_info(self):
        """查找信息"""
        find_name = input("输入搜索的用户名:")
        flag = 0  # 0,没有找到,1找到了
        for name in self.names:
            for value in name.values():
                if find_name == value:
                    flag = 1
                    print("找到了:{}".format(find_name))
                    break

        if flag == 0:
            print("没有找到:{}".format(find_name))

    def show_info(self):
        """表格方式显示所以信息"""
        print("\n")
        print("当前用户信息")
        print("~" * 50)
        print("\t姓名\t\t\t电话\t\t\t密码\t")
        for name in self.names:
            msg = "\t" + name.get("name") + "\t\t" + name.get("phone") + "\t\t" + name.get("wechat") + "\t\t"
            print("~" * 50)
            print(msg)
        print("~" * 50)
        print("\n")

    def del_names(self):
        self.names.clear()

    # 程序的主要逻辑和程序入口
    def start(self):
        print_menu()
        # 加载文件中保存的信息,加载到内存中
        self.load_info()
        while True:
            print("\n\n")
            print("操作指令")
            print("~" * 50)
            print(self.info)
            print("~" * 50)
            number = input("请按照上面的提示输入相应指令:")

            # 判断是否输入是纯的数字
            if number.isdigit():
                number = int(number)
                if number == 1:
                    # 添加信息
                    self.add_info()
                elif number == 2:
                    # 删除信息
                    self.delete_info()
                elif number == 3:  # 修改
                    # 修改信息
                    self.modify_info()
                elif number == 4:  # 查找
                    # 查找信息
                    self.find_info()
                elif number == 5:
                    # 显示信息
                    self.show_info()
                elif number == 7:
                    # 登录
                    self.login()
                elif number == 0:
                    self.del_names()
                elif number == 6:
                    break

            else:
                print("请输入正确的编号!")

    # 运行的时候,读取保存在文件的信息,并且赋值给names,第一次读文件,文件不存在,"r"会报错,"a+"
    def load_info(self):
        f = open("students.txt", "a+")
        f.seek(0, 0)
        content = f.read()
        # print("content==",content)
        if len(content) > 0:
            self.names = eval(content)
            logging.info(content)

    # 每次删除或者修改或者增加都重新保存数据,覆盖保存w
    def save_info(self):
        f = open("students.txt", "w")
        f.write(str(self.names))
        f.close()

s = StudentSys()
s.start()
