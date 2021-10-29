from os import name
import sqlite3
from flask import Flask, render_template, blueprints, request, session, flash
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db
from markupsafe import escape
import random
import functools


main = blueprints.Blueprint('main', __name__) #blue prints permite separar la app en diferentes plantillas #




def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'session_key' not in session:#puedes hacer otro tipo de validación 
            return redirect(url_for('main.index'))
        return view(**kwargs)

    return wrapped_view

# @main.route('/prueba')
# @login_required
# def prueba():
#     return render_template('feed_prueba.html')  ## solo demostracion practica (eliminar para produccion)


# aqui se puede poner otro atributo (methods=['GET´, 'POST'])#
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/hacerLogin',  methods=['POST'])
def hacerLogin():
    
    if request.method == 'POST':
        username = request.form['usuario']
        clave = request.form['clave']

        #sql = "select * from Usuario where username = '{0}' and clave = '{1}'".format(username,clave) ##0 y 1 hacen referencia a "username y clave rescpectivamente"
        db= get_db()

        user = db.execute("select * from Usuario where username = ? ",(username,)).fetchone() ##para seleccionar un usuario de la base de datos que cumpla con la criteria
        
        if user is not None:
            clave = clave + username
            sw = check_password_hash(user[7],clave)
        
            if(sw):
                session['session_key'] = user[0]
                session['username'] = user[3]
                session['nombre'] = user [1]
                session['role'] = user[8]

                return redirect(url_for('main.feed'))
        
        
        # flash('Usuario o clave incorrecto.')   pendiente por agregar
        
            
    return render_template('index.html') #cuando se manda get.


@main.route('/logout')
def logout():
    session.clear() #se destruye la sesion. 
    return redirect(url_for('main.index'))

@main.route('/feed/')
@login_required
def feed():

    return render_template('feed.html')


@main.route('/register/', methods=['POST','GET'])
def register():
    
    if request.method == 'POST':
        nombres = escape(request.form['nombre'])
        apellidos = escape(request.form['apellido'])
        email = escape(request.form['correo'])
        username = escape(request.form['usuario'])
        clave = escape(request.form['clave'])
        dob = escape(request.form['fecha'])
        sexo = escape(request.form['sex'])
        role = "user" 
        
        #sql= "insert into Usuario(nombres, apellidos, username, email, sexo, dob, clave) values('{0}','{1}','{2}','{3}','{4}', '{5}', '{6}')".format( nombres, apellidos, username, email , sexo, dob, clave )
        db = get_db()
        clave = clave + username # tipo de salt 
        clave= generate_password_hash(clave) #aqui se se usa el metodo para crear el hash sobre la clave
        db.execute("insert into Usuario(nombres, apellidos, username, email, sexo, dob, clave, role) values( ?, ?, ?, ? ,? ,?, ? ,?)",( nombres, apellidos, username, email ,sexo , dob, clave, role))
        db.commit()

        print("registro exitoso")
        return redirect(url_for('main.index'))

    return render_template('registro.html')
    

@main.route('/user_space/')
@login_required
def mi_espacio():
    return render_template('mi_espacio.html')


@main.route('/search_results/')
@login_required
def resultados():
    db = get_db()
    cur = db.cursor()
    sql = "SELECT * FROM Usuarios"
    cur.execute("select * from Usuario")
    info_resultados = cur.fetchall()
    cur.close
    

    return render_template('search_result.html',usuarios = info_resultados) #no se estan mostrando los resultados en el html


@main.route('/explore/')
@login_required
def explorar():
    return render_template('explorar.html')


@main.route('/admin_profile/')
@login_required
def admin_user():
    return render_template('admin_profile.html')


@main.route('/admin_dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')


@main.route('/messages/')
@login_required
def mensajes():
    return render_template('mensajes.html')


@main.route('/alerts/')
def notificaciones():
    return render_template('notificaciones.html')


@main.route('/new_post/')
@login_required
def post():
    return render_template('nuevo_post.html')


@main.route('/user_profile/')
@login_required
def perfil_user():
    return render_template('user_profile.html')


@main.route('/new_password/')
@login_required
def newpass():
    return render_template('cambPassword.html')


@main.route('/suggestions/')
@login_required
def relacionate():
    return render_template('relacionate.html')
