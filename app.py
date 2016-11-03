from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models import db

from models.blog import Blog
from models.user import User
from models.comment import Comment

app = Flask(__name__)
db_path = 'blog.sqlite'
manager = Manager(app)


def register_routes(app):
    from routes.blog import main as routes_blog
    from routes.auth import main as routes_auth

    app.register_blueprint(routes_blog, url_prefix='/blog')
    app.register_blueprint(routes_auth, url_prefix='/auth')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pwd@localhost/bbs'
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


# 自定义的命令行命令用来运行服务器
@manager.command
def server():
    print('server run')
    # app = configured_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def configure_manager():
    """
    这个函数用来配置命令行选项
    """
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()
"""
gunicorn -b '0.0.0.0:80' redischat:app
python app.py db init
python app.py db migrate
python app.py db upgrade
python app.py server
"""
