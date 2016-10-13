from . import ModelMixin
from . import db
from . import cur_time
import json


class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    # user_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref="blog")

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = cur_time()

    def json(self):
        j = {
            'id': self.id,
            'task': self.task,
            'created_time': self.created_time,
        }
        return json.dumps(j, ensure_ascii=False)
