import datetime
import json
import requests


class WechatRobot(object):
    """企业微信机器人"""
    URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6f6baff6-6e57-4ff5-b1b3-1c6d503a4c17"  # Webhook地址

    def text_message(self, content):
        data = {
            "msgtype": "text",
            "text": {
                "mentioned_mobile_list": ['@all'],
                "content": content
                # "mentioned_list": ["jiangan"],
            }
        }
        data = json.dumps(data, ensure_ascii=False)
        data = data.encode(encoding="utf-8")
        r = requests.post(url=self.URL, data=data)
        r = json.loads(r.text)
        return r

    def markdown_message(self):
        reger = {
            "msgtype": "markdown",
            "markdown": {

                "content": "实时新增广州本土疫情<font color=\"warning\">3</font>例，请相关同事注意。\n"
                           ">类型:<font color=\"comment\">广州疫情</font> \n"
                           ">新增无症状:<font color=\"warning\">1</font>例 \n"
                           ">现有确诊:<font color=\"warning\">147</font>例"
            }
        }

        data = json.dumps(reger, ensure_ascii=False)
        data = data.encode(encoding="utf-8")
        r = requests.post(url=self.URL, data=data)
        r = json.loads(r.text)
        return r


if __name__ == "__main__":
    # print(WechatRobot().message(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print(WechatRobot().markdown_message())
    # {'errcode': 0, 'errmsg': 'ok'}
