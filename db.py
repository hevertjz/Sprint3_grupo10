import sqlite3 
from sqlite3 import Error
from flask import current_app, g
def get_db():
    try:
        if 'db' not in g:
            print('base de datos conectada')
            g.db = sqlite3.connect('cairina_2.0.db')
            return g.db
    except Error:
        print(Error)


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()