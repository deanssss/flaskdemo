import json

from flask import Blueprint, request
from app import db
from model.task import Task
from util.json_util import serialize, make_json_rsp, make_simple_rsp

todo = Blueprint("todo", __name__, url_prefix="/todo")


@todo.route('/listTasks', methods=['POST', 'GET'])
def list_tasks():
    tasks = Task.query.all()
    return make_json_rsp({
        "tasks": [serialize(t) for t in tasks],
        "total": len(tasks)
    })


@todo.route('/addTask', methods=['POST'])
def add_task():
    data = request.get_json()
    print("title: " + data['title'] + ", content: " + data['content'])
    task = Task()
    task.title = data['title']
    task.content = data['content']
    task.state = 0
    db.session.add(task)
    db.session.commit()
    return make_simple_rsp(0, "添加成功")


@todo.route('/deleteTask', methods=['POST'])
def delete_task():
    data = request.get_json()
    print("id: " + str(data['id']))
    task = Task.query.get(int(data['id']))
    db.session.delete(task)
    db.session.commit()
    return make_simple_rsp(0, "删除成功")

