from flask import Flask, request, make_response, redirect, abort, render_template
# from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
import sqlalchemy
import sqlite3

# секция комментариев
# функция redirect() перенаправляет на другой сайт, принимает url
# функция abort() обрабатывает ошибки,принимает код ошибки
import view

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# manager = Manager(app)

@app.route("/")
def index():
    return render_template("index.html", current_time=datetime.utcnow())


@app.route("/user/<name>")
def user(name):
    if name == "Nik":
        abort(400)
    else:
        return render_template("user.html", name=name)


@app.route("/bad/")
def bad():
    return redirect("http://ya.ru")


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.errorhandler(500)
def enternal_server_error(err):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
