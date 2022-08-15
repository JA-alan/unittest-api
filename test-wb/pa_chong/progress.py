from urllib.request import urlopen, Request
import MyPyClass

url = 'https://www.baidu.com'  # 爬取的网页地址
ua = MyPyClass.GetUserAgent()  # 获取一个User-Agent
request_setting = Request(url, headers={'User-Agent': ua})  # 设置请求参数的设置————伪装
response = urlopen(request_setting, timeout=20)  # 响应对象
content = response.read().decode('utf-8')
# decode编码，需要根据页面实际编码进行修改，某些页面是gbk编码的
print(content)  # 爬取的实际页面内容
print('-' * 100)  # 打印分隔符
print(response.getcode())  # 响应状态码
print(response.geturl())  # 爬取的地址
print(response.info())  # 响应信息
