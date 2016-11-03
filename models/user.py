from . import ModelMixin
from . import db
from . import cur_time
import json


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    # brief = db.Column(db.String())
    # created_time = db.Column(db.Integer, default=0)
    # node 外键
    # node_id = db.Column(db.String(), db.ForeignKey('nodes.id'))
    # user_id = db.Column(db.Integer)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # comments = db.relationship('Comment', backref="blog")

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        # self.brief = form.get('brief', '')
        # self.node = form.get('node', '')
        # self.created_time = cur_time()

    def json(self):
        j = {
            'id': self.id,
            'username': self.username,
            'password': self.password,
        }
        return json.dumps(j, ensure_ascii=False)

    def login_satisfied(self, user):
        if user is not None:
            username_satisfied = user.username == self.username
            password_satisfied = user.password == self.password
            return username_satisfied and password_satisfied
        return False

    def register_satisfied(self):
        valid_username = User.query.filter_by(username=self.username).first() is None
        valid_username_len = len(self.username) >= 6
        valid_password_len = len(self.password) >= 6
        # valid_captcha = self.captcha == '3'
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        elif not valid_username_len:
            message = '用户名长度必须大于等于 6'
            msgs.append(message)
        elif not valid_password_len:
            message = '密码长度必须大于等于 6'
            msgs.append(message)
        # elif not valid_captcha:
        #     message = '验证码必须输入 3'
        #     msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len # and valid_captcha
        return status, msgs
