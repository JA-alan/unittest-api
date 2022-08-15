import time, os, sched
import pytest


# while True:
#     time_new = time.strftime("%H:%M:%S", time.localtime())
#     if time_new == "17:19:10":
#         print("hello")
#         time.sleep(2)
#         subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"定時發送"
#         print(subject)

#
# schedule = sched.scheduler(time.time, time.sleep)
#
#
# def perform_command(cmd, inc):
#     # enter 计划多少秒后，再次启动自己并进行运行
#     a = schedule.enter(inc, 0, perform_command, (cmd, inc))
#     os.system(cmd)
#     time_new = time.strftime("%H:%M:%S", time.localtime())
#
#     if "17:26:10" > time_new < "17:27:10":
#         print("hello")
#     elif time_new > "27:27:10":
#         schedule.cancel(a)
#
#
# def timming_exe(cmd, inc=60):
#     schedule.enter(inc, 5, perform_command, (cmd, inc))
#     schedule.run()
#
#
# print(" 调试 ")
# timming_exe("echo %time%", 2)

# content of test.py


# class TestClass(object):
#     def test_zne(self):
#         x = "this"
#         assert 'h' in x
#
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, 'check')
#
#     def test_a(self):
#         assert 1 == 2
#

# if __name__ == "__main__":
#     pytest.main('-s', 'pytest_run.py')

# -*- coding: utf-8 -*-
import hashlib

# 待加密内容
strdata = "xiaojingjiaaseafe16516506ng"

h1 = hashlib.md5()
h1.update(strdata.encode(encoding='utf-8'))

strdata_tomd5 = h1.hexdigest()

print("原始内容：", strdata, ",加密后：", strdata_tomd5)

import time
import base64
import hmac


# 生产token
def generate_token(key, expire=3600):
    r'''
        @Args:
            key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
            expire: int(最大有效时间，单位为s)
        @Return:
            state: str
    '''
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


# 验证token
def certify_token(key, token):
    r'''
        @Args:
            key: str
            token: str
        @Returns:
            boolean
    '''
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
    # token certification success
    return True


key = "xiaojingjing"
print("key：", key)
user_token = generate_token(key=key)

print("加密后1：", user_token)
user_de = certify_token(key=key, token=user_token)
print("验证结果：", user_de)

key = "xiaoqingqing"
user_de = certify_token(key=key, token=user_token)
print("验证结果：", user_de)
