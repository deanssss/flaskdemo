# Flask App 的扩展
import config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# from qiniu import Auth

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
# qin = Auth(config.QINIU_ACCESS_KEY, config.QINIU_SECRET_KEY)