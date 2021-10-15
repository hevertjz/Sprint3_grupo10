from flask import Flask, render_template, blueprints, request
from flask.helpers import url_for
from werkzeug.utils import redirect

main = blueprints.Blueprint('main', __name__)


# aqui se puede poner otro atributo (methods=['GET´, 'POST'])#
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/hacerLogin',  methods=['POST'])
def hacerLogin():
    print(request.method)
    if request.method == 'POST':
        return redirect(url_for('main.feed'))
    return render_template('feed.html')


@main.route('/feed/')
def feed():
    return render_template('feed.html')


@main.route('/register/')
def register():
    return render_template('registro.html')


@main.route('/user_space/')
def mi_espacio():
    return render_template('mi_espacio.html')


@main.route('/search_results/')
def resultados():
    return render_template('search_result.html')


@main.route('/explore/')
def explorar():
    return render_template('explorar.html')


@main.route('/admin_profile/')
def admin_user():
    return render_template('admin_profile.html')


@main.route('/admin_dashboard/')
def dashboard():
    return render_template('dashboard.html')


@main.route('/messages/')
def mensajes():
    return render_template('mensajes.html')


@main.route('/alerts/')
def notificaciones():
    return render_template('notificaciones.html')


@main.route('/new_post/')
def post():
    return render_template('nuevo_post.html')


@main.route('/user_profile/')
def perfil_user():
    return render_template('user_profile.html')


@main.route('/new_password/')
def newpass():
    return render_template('cambPassword.html')


@main.route('/suggestions/')
def relacionate():
    return render_template('relacionate.html')
