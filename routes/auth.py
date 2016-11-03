from models.user import User
from routes import *
# for decorators
from functools import wraps

main = Blueprint('auth', __name__)
Model = User
self_id = id


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        print('admin required')
        if request.args.get('uid') != '1':
            print('not admin')
            abort(404)
        return f(*args, **kwargs)
    return function


@main.route('/')
def index():
    # ms = Model.query.all()
    return render_template('auth.html')


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    user = u.query.filter_by(username=u.username).first()
    if u.login_satisfied(user):
        session.permanent = True
        session['user_id'] = user.id
        return redirect('/blog')
    return redirect(url_for('.index'))


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    if u.register_satisfied():
        u.save()
        session.permanent = True
        session['user_id'] = u.id
        return redirect('/blog')
    else:
        return redirect(url_for('.index'))
