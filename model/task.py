from app import db
from util import date_util


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createdTime = db.Column(db.String(30), default=date_util.now_datetime_str)
    completedTime = db.Column(db.String(30))
    title = db.Column(db.String(30))
    content = db.Column(db.String(100))
    state = db.Column(db.Integer, default=0)

    def complete(self):
        self.state = 1
        self.completedTime = date_util.now_datetime_str()
