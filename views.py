from os import name
import sqlite3
from flask import Flask, render_template, blueprints, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db
import random


main = blueprints.Blueprint('main', __name__) #blue prints permite separar la app en diferentes plantillas #


# aqui se puede poner otro atributo (methods=['GET´, 'POST'])#
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/hacerLogin',  methods=['POST'])
def hacerLogin():
    print(request.method)
    if request.method == 'POST':
        username = request.form['usuario']
        clave = request.form['clave']

        #sql = "select * from Usuario where username = '{0}' and clave = '{1}'".format(username,clave) ##0 y 1 hacen referencia a "username y clave rescpectivamente"
        db= get_db()

        user = db.execute("select * from Usuario where username = ? ",(username,)).fetchone() ##para seleccionar un usuario de la base de datos que cumpla con la criteria
        
        if user is not None:
            clave = clave + username
            sw = check_password_hash(user[6],clave)
            #print("credenciales correctas para " + user[3])
            if(sw):
                return render_template('feed.html')
            
        else: 
            print("usuario y/o clave incorrectos")
            return render_template('index.html')
            
        ##return redirect(url_for('main.feed'))
    return render_template('feed.html')


@main.route('/feed/')
def feed():
    sql= "select username from Usuario"
    db= get_db()
    resultados = []
    resultados.append (db.execute(sql))
    print(resultados)

    return render_template('feed.html')


@main.route('/register/', methods=['POST','GET'])
def register():
    
    if request.method == 'POST':
        nombres = request.form['nombre']
        apellidos = request.form['apellido']
        email = request.form['correo']
        username = request.form['usuario']
        clave = request.form['clave']
        dob = request.form['cumpleaños']
        sexo = request.form['sex']
        
        #sql= "insert into Usuario(nombres, apellidos, username, email, sexo, dob, clave) values('{0}','{1}','{2}','{3}','{4}', '{5}', '{6}')".format( nombres, apellidos, username, email , sexo, dob, clave )
        db = get_db()
        clave = clave + username
        clave= generate_password_hash(clave) #aqui se se usa el metodo para crear el hash sobre la clave
        db.execute("insert into Usuario(nombres, apellidos, username, email, sexo, dob, clave) values( ?, ?, ?, ? ,? ,?, ?)",( nombres, apellidos, username, email ,sexo , dob, clave))
        db.commit()
        
        print("registro exitoso")

    return render_template('registro.html')
    
# @main.route('/register/enviar_registro/', methods =['POST' ,'GET'])
# def enviar_registro():





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
