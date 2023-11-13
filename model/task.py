from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    content = db.Column(db.String(100))
    state = db.Column(db.Integer)

    def change_state(self, state):
        self.state = state
