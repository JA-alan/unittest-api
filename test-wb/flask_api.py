from flask import Flask, jsonify, request, make_response
from flask import abort
from flask_test import login

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False,
        'message': '查询成功'
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET', 'POST'])
def get_task(task_id):
    if request.method == 'GET':
        # task = filter(lambda t: t['id'] == task_id, tasks)
        task_id = task_id - 1
        try:
            int(task_id)
            # if task_id != int(task_id):
            #     return abort(404)
            return jsonify({'task': tasks[task_id]})

        except Exception as e:
            return not_found(e)

    elif request.method == 'POST':
        pass


@app.route('/todo/api/v1.0/taskss', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
