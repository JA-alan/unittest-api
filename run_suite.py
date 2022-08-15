import unittest
import ddt
from lib.sendrequest import send_requests
from lib.utlis import *
from setting import case_root


def case_data(dataname) -> list:
    """
    处理测试用例数据
    :param dataname: 测试用例文件名
    :return: 测试用例数据
    """
    test_case = case_root + '/{}.xlsx'.format(dataname)  # case_root ——为存放测试用例的路径
    test_num = Excel('r', test_case).read()
    testdata = excel_dict(test_num)
    return testdata


@ddt.ddt
class TestCase(unittest.TestCase):

    @ddt.data(*case_data('testcase'))
    def test_run_case(self, data):
        self.return_ = """
        执行测试脚本
        :param data: 参数化后测试用例|dict类型
        :return:
        """
        self.response = send_requests(data)  # 返回response
        #  self.cookie = send_requests()
        print('________')
        self.result = self.response.json()
        # print(self.result)
        # code = data['code']  # 获取表内code
        # status = data['status']  # 获取表内状态码
        # msg = data['msg']  # 获取响应状态
        # if code == self.result['code'] and status == self.response.status_code \
        #         and msg == self.result['msg']:  # 判断返回数据是否和表内数据相同
        #     self.msg_data = "PASS"
        # else:
        #     self.msg_data = "FAIl"
        #     # results_root ———为写入文件存放的路径（setting.py内的变量）
        # Excel('w', '../results/results.xlsx') \
        #     .write(write_result(value7=str(self.result), value8=self.msg_data))
        # self.assertEqual(self.result['code'], code)
        # self.assertEqual(self.response.status_code, status)
        # self.assertEqual(self.result['msg'], msg)


if __name__ == "__main__":
    unittest.main()
