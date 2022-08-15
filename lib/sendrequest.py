import logging

from requests.packages import urllib3 as url3
import requests
from data.data_driven import data_association, write_data


def send_requests(apidata):
    """
    分析测试用例自带参数、发送请求
    :param apidata: 测试用例
    :return:
    """
    # logging.info('标题为{}'.format(apidata['id']))
    try:
        # 从读取的表格中获取响应的参数作为传递
        method = apidata["get_type"]
        url = apidata["url"]
        # 判断字典内请求头是否为空
        if apidata["header"] == '':
            # 返回None
            header = None
        else:
            # 将值处理后用做请求参数
            header = eval(data_association(apidata['header']))
        # 判断字典内测试数据是否为空
        if apidata["data"] == "":
            # 返回None
            body_data = None
        else:
            # 将值处理后用做请求参数
            body_data = eval(data_association(apidata['data']))  # 新增数据关联的处理
            # body_header =eval(data_association(apidata["header"]))

            # logging.info('请求头{}'.format(body_header))
        s = requests.session()

        url3.disable_warnings()
        # logging.info('请求url:{}'.format('https://tapi.apbenben.com/benben-dubbo-web'+ url))
        logging.info('请求参数:{}'.format(body_data))  # 新增打印参数log，方便查看

        # logging.info('请求头:{}'.format(header))
        if method == 'get':
            re = s.request(method=method, url='https://tapi.apbenben.com/benben-dubbo-web'
                                              + url, headers=header, params=body_data,
                           verify=False)  # 将对应的数据填入相应位置返回res
        elif method == 'post':
            re = s.request(method=method, url='https://tapi.apbenben.com/benben-dubbo-web'
                                              + url, headers=header, json=body_data,
                           verify=False)

        else:

            raise Exception("请求格式有误")
        # logging.info('请求结果:{}'.format(re.json()))  # 新增打印参数log，方便查看

        ruleName = apidata['rule_name']
        ruleValue = apidata['rule_value']

        write_data(apidata['precondition'], ruleName, ruleValue, body_data, re.json(), re.headers)

        return re

    except Exception as error:
        logging.error("错误信息1", error)


if __name__ == '__main__':
    case_dict = {'id': 1, 'get_type': 'post', 'interface': '相加接口',
                 'title': '参数正常-成功', 'header': '', 'url': '/login/login',
                 'data': "{'account': 'jiangan', 'password': 'asd123'}",
                 'expected': "{'code': 0, 'msg': 'ok', 'value': 3}", 'code': 0,
                 'status': 200, 'msg': 'ok', 'precondition': '', 'rule_name': '', 'rule_value': ''}
    case_dict1 = {'id': 1, 'get_type': 'get', 'interface': '相加接口',
                  'title': '参数正常-成功', 'header': '', 'url': '/add',
                  'data': "{'a': '1', 'b': '2'}",
                  'expected': "{'code': 0, 'msg': 'ok', 'value': 3}", 'code': 0,
                  'status': 200, 'msg': 'ok', 'precondition': '', 'rule_name': '', 'rule_value': ''}

    re = send_requests(case_dict)
    print(re.url)
    print(re)
    print(re.json())
    print(re.cookies)
