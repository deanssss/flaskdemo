from flask import Flask

import config
from extension import db, login_manager
from module.auth import auth
from module.test import test
from module.todo import todo

# 初始化Flask
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
login_manager.init_app(app)

# 注册模块
app.register_blueprint(auth)
app.register_blueprint(test)
app.register_blueprint(todo)


# 启动服务
if __name__ == '__main__':
    app.run()


@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    from model.user import User
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象


@app.context_processor
def inject_user():
    from model.user import User
    user = User.query.first()
    return dict(user=user)  # 注入给模版的上下文环境中，避免重复代码


# noinspection PyUnresolvedReferences
import commands
# noinspection PyUnresolvedReferences
import home
# noinspection PyUnresolvedReferences
import errors