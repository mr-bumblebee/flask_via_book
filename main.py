from flask import Flask, request, make_response, redirect, abort, render_template, session, \
    url_for, flash
# from flask_script import Manager
from flask_bootstrap import Bootstrap
#library for work with local date/time
from flask_moment import Moment
#library for work with web form


from datetime import datetime
#config file
from config import Configuration
from Forms import NameForm

import sqlite3

# секция комментариев
# функция redirect() перенаправляет на другой сайт, принимает url
# функция abort() обрабатывает ошибки,принимает код ошибки
import view

app = Flask(__name__)
app.config.from_object(Configuration)
bootstrap = Bootstrap(app)
moment = Moment(app)

# manager = Manager(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session["name"]
        if old_name is not None and old_name != form.name.data:
            flash("You changed name")
        session["name"] = form.name.data
        form.name.data = ''
        return redirect(url_for("index"))
    return render_template("index.html",
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session["name"])


@app.route("/user/<name>")
def user(name):
    if name == "Nik":
        abort(400)
    else:
        return render_template("user.html", name=name)


@app.route("/webform")
def webform():
    return render_template("webform.html", form=NameForm())

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
