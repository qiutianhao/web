from models.blog import Blog
from routes import *

main = Blueprint('blog', __name__)
Model = Blog
self_id = id


@main.route('/')
def index():
    m = Model.query.all()
    return render_template('index.html', ms=m)


@main.route('/add_view')
def add_view():
    return render_template('add.html')


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.index'))


@main.route('/delete/<int:m_id>')
def delete(m_id):
    m = Model.query.get(m_id)
    m.delete()
    return redirect(url_for('.index'))


@main.route('/edit_view/<int:m_id>')
def edit_view(m_id):
    m = Model.query.get(m_id)
    return render_template('edit.html', m=m)


@main.route('/edit/<int:m_id>', methods=['POST'])
def edit(m_id):
    m = Model.query.get(m_id)
    m.delete()
    form = request.form
    t = Model(form)
    t.save()
    return redirect(url_for('.index'))