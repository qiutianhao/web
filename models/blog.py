from . import ModelMixin
from . import db
from . import cur_time
import json


class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    brief = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    node = db.Column(db.String())
    # node 外键
    # node_id = db.Column(db.String(), db.ForeignKey('nodes.id'))
    # user_id = db.Column(db.Integer)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref="blog")

    def __init__(self, form):
        self.content = form.get('content', '')
        self.brief = form.get('brief', '')
        self.title = form.get('title', '')
        self.node = form.get('node', '')
        self.created_time = cur_time()

    def json(self):
        j = {
            'id': self.id,
            'content': self.content,
            'created_time': self.created_time,
        }
        return json.dumps(j, ensure_ascii=False)
