from flask import Flask
# config file
from config import Configuration
# from flask_script import Manager
from flask_bootstrap import Bootstrap
# library for work with local date/time
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)  # configuration app
print(Configuration.SQLALCHEMY_DATABASE_URI)
bootstrap = Bootstrap(app)  # permit using CSS styles from Bootstrap
moment = Moment(app)  # permit using UTC
db = SQLAlchemy(app, engine_options={"connect_args": {'check_same_thread': False}})  # create
# database


def db_sel():
    import sqlite3
    conn = sqlite3.connect("database.db")
    #conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    sql = "SELECT * FROM roles"
    cursor.execute(sql)
    print(cursor.fetchall())
    conn.close()
# manager = Manager(app)