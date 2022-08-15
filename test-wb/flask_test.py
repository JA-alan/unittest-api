import datetime
import json
from dbSql import DB_SQL
from flask import Flask, url_for, request, render_template, redirect, session, jsonify, make_response
import time
import hashlib
from threading import Timer


ALLOWED_HOSTS = ["*", ]
app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'


def initialization_token(name=None):
    flag = 0
    while flag == 1:

        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        t = Timer(10, initialization_token)
        t.start()
        flag += 1
        DB_SQL().logout_del_token(name)


def t_stamp():
    """转换时间格式"""
    t = time.time()
    t_tamp = int(t)
    return t_tamp


def token():
    """生成token"""
    API_SECRET = 'JIANGAN'
    project_code = "test"
    account = "jiangan"
    time_stamp = str(t_stamp())
    h1 = hashlib.md5()
    strs = project_code + account + time_stamp + API_SECRET
    h1.update(strs.encode("utf-8"))
    user_token = h1.hexdigest()
    return user_token


@app.route('/index')  # 首页
def index():
    return 'way welcome the python'


@app.route('/logon/register', methods=['POST'])
def register():  # 注册
    get_data = request.args.to_dict()
    user = get_data.get('user')
    password = get_data.get('password')
    phone = get_data.get('phone')
    result = DB_SQL().insert_user(user, password, phone)
    if result == "插入失败":
        return {'return_code': '405', 'return_info': '账号%s已被注册' % user}
    else:

        DB_SQL().insert_news()
        return_dict = {'return_code': '200', 'return_info': '注册成功', 'name': user}
        return json.dumps(return_dict, ensure_ascii=False)


@app.route('/login', methods=['GET', 'POST'])
def login():  # 登录
    if request.method == 'POST':
        get_data = request.args.to_dict()
        name = get_data.get('user')
        password = get_data.get('password')
        return_dict = {}
        if len(request.args) == 0:
            return_dict['return_code'] = '5004'
            return_dict['return_info'] = '参数请求为空'
            return json.dumps(return_dict, ensure_ascii=False)

        elif len(request.get_data()) > 2:
            return_dict['return_code'] = '403'
            return_dict['return_info'] = '请求参数错误'
            return json.dumps(return_dict, ensure_ascii=False)

        elif name is None:
            return_dict['return_code'] = '404'
            return_dict['return_info'] = '请求错误'
            return json.dumps(return_dict, ensure_ascii=False)
        elif password is None:
            return_dict['return_code'] = '404'
            return_dict['return_info'] = '请求错误'
            return json.dumps(return_dict, ensure_ascii=False)
        else:
            return_dict = {'return_code': '200', 'return_info': '处理成功',
                           'result': "用户 %s 登录成功" % name,
                           "login_time": datetime.datetime.now().strftime("%Y-%m-%d %H-%M:%S"),
                           "token": token(),
                           "data": DB_SQL().api_select(name, password)
                           }
            return jsonify(return_dict)

    elif request.method == 'GET':
        get_data = request.args.to_dict()
        name = get_data.get('user')
        password = get_data.get('password')
        return_dict = {}
        if name is None:
            return_dict['return_code'] = '404'
            return_dict['return_info'] = '请求错误'
            return json.dumps(return_dict, ensure_ascii=False)
        elif password is None:
            return_dict['return_code'] = '404'
            return_dict['return_info'] = '请求错误'
            return json.dumps(return_dict, ensure_ascii=False)
        elif len(request.args) == 0:
            return_dict['return_code'] = '403'
            return_dict['return_info'] = '参数请求为空'
            return json.dumps(return_dict, ensure_ascii=False)

        elif len(request.args) > 2:
            return_dict['return_code'] = '404'
            return_dict['return_info'] = '请求错误'
            return json.dumps(return_dict, ensure_ascii=False)
        if len(request.args) == 2:
            return_dict = {'return_code': '200', 'return_info': '处理成功',
                           'result': "用户 %s 登录成功" % name,
                           "login_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                           "token": token(),
                           "data":DB_SQL().api_select(name, password)
                           }
            initialization_token(name)
            now_token = return_dict["token"]
            DB_SQL().token_data(now_token, name)
            if return_dict["data"] == {"code": 402, "result": "账号或密码错误"}:
                return {"code": 402, "result": "账号或密码错误"}
            return jsonify(return_dict)

        else:
            return DB_SQL().api_select(name, password)
    # if 'user' in session:
    #     return "hello %s！" % session['user']
    # else:
    #     title = request.args.get('title', 'Default')
    #     return render_template('login.html', title=title)


@app.route('/logout', methods=['GET'])
def logout():  # 退出登录
    if request.method == 'GET':
        get_data = request.args.to_dict()
        user = get_data.get('user')
        token = get_data.get('token')
        if len(request.args) == 2:
            session.pop('user', None)
            result = DB_SQL().check_users_token(token, user)
            if result == {'return_code': '200'}:
                DB_SQL().logout_del_token(user)
                return {'result': '%s成功退出登录' % user}
            elif result == {'result': '!='}:
                return json.dumps({'return_code': '400', 'return_info': '用户未登录'})

        elif len(request.args) > 2:
            return {"return_code": 415, "return_info": "请求错误"}
        elif len(request.args) < 2:
            return {"return_code": 415, "return_info": "请求错误"}
        else:
            dict_txt = {'result': '%s成功退出登录1' % user}
            DB_SQL().logout_del_token(user)
            return json.dumps(dict_txt, ensure_ascii=False)


@app.route('/user/update', methods=['post'])
def update_user_profile():  # 修改个人信息
    get_data = request.args.to_dict()
    name = get_data.get('name')
    age = get_data.get('age')
    character = get_data.get('character')
    Token = get_data.get('token')
    result = DB_SQL().check_news_token(Token)
    if result == {'return_code': '400', 'return_info': '用户未登录'}:
        return {'return_code': '400', 'return_info': '用户未登录'}

    elif result == {'return_code': '200'}:
        DB_SQL().data_update(Token, name, age, character)
        return_dict = {'return_code': '200', 'return_info': '修改成功'}
        return json.dumps(return_dict, ensure_ascii=False)


@app.route('/user/alluser/list', methods=['post'])  # 查询所有用户信息
def all_user_list():
    get_data = request.args.to_dict()
    uid = get_data.get('code')
    result = DB_SQL().check_uid(uid)
    if result == {"code": 200, "result": "check"}:
        result = {"return_code": 200, "data": DB_SQL().select_all()}
        return json.dumps(result, ensure_ascii=False)
    elif result == {"code": 200, "result": "no check"}:
        return json.dumps({"return_code": "401", "return_info": "没有权限"}, ensure_ascii=False)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6000)
