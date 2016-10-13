from . import ModelMixin
from . import db
from . import cur_time


class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.String())
    # user_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = cur_time()

    # def username(self):
    #     un = User.query.filter_by(id=self.user_id).first().username
    #     return un
