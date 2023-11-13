# Flask App 的配置文件
import os

# 数据库配置
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv('SECRET_KEY', 'dev')

QINIU_ACCESS_KEY = 'zH1aaDlDk9v0RDaE9CFCndb2hzH382jkuf9k5Vc2' # os.getenv('QINIU_ACCESS_KEY', 'unknown')
QINIU_SECRET_KEY = 'DorjbiCs2FSsmSE3hExwOrs17Vr3tfrIaoDD3CVH' # os.getenv('QINIU_SECRET_KEY', 'unknown')