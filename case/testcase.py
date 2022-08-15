import logging
import unittest
import ddt
import time
from lib.sendrequest import send_requests
from lib.utlis import Excel, excel_dict, write_result


def case_data(dataname) -> list:
    """
    处理测试用例数据
    :param dataname: 测试用例文件名
    :return: 测试用例数据
    """
    test_case = '../database/{}.xlsx'.format(dataname)
    test_num = Excel('r', test_case).read()
    testdata = excel_dict(test_num)
    return testdata


@ddt.ddt
class TestCase(unittest.TestCase):

    @ddt.data(*case_data('testcase'))
    def test_run_case(self, data):
        """
        执行测试脚本
        :param data: 参数化后测试用例|dict类型
        :return:
        """
        response = send_requests(data)  # 返回response
        print('_____________________')  # 没有实际意义- -
        logging.info("页面返回信息：%s" % response.json())
        import warnings
        warnings.simplefilter("ignore", ResourceWarning)

        self.result = response.json()

        code = int(data['code'])  # 获取表内code
        code = str(code)
        status = data['status']  # 获取表内状态码
        msg = data['message']  # 获取响应状态
        # and msg == self.result['message']:  # 判断返回数据是否和表内数据相同
        if code == self.result['code'] and status == response.status_code:
            self.msg_data = "PASS"  # 这个值要用来写入
        else:
            self.msg_data = "FAIl"  # 这个值要用来写入
        Excel('w', '../results/results.xlsx') \
            .write(write_result(value4=response.url, value7=str(self.result), value8=self.msg_data))
        # 写入时需转换为str类型 （两个参数为例）
        self.assertEqual(self.result['code'], code)
        self.assertEqual(response.status_code, status)
        # self.assertEqual(self.result['message'], msg)


if __name__ == "__main__":
    while True:
        time_new = time.strftime("%H:%M:%S", time.localtime())
        if time_new == "15:19:10":
            print("hello")
            subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "定時發送"
            print(subject)
            time.sleep(2)
            unittest.main()
