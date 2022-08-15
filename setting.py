import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) #项目根目录
LOG_PATH = os.path.join(PROJECT_ROOT, 'log', 'api_test.log')  # 日志路径

BASE_URL = "http://127.0.0.1:8000"  # 本地url
BASE_URL_dev = 'http://127.0.0.1:8000'  # 假装一下url不同
BASE_URL_uat = 'http://127.0.0.1:8000'  # 假装一下url不同


case_root = os.path.join(PROJECT_ROOT, 'database')  # 测试用例
results_root = os.path.join(PROJECT_ROOT, 'results', 'results.xlsx')#测试结果
REPORT_PATG = os.path.join(PROJECT_ROOT, 'report', 'index.html')  # 报告路径

TEST_JSON = os.path.join(PROJECT_ROOT, 'database', 'test_data.txt')  #存放接口返回数据
