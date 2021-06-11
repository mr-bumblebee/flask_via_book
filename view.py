from app import app

# функция redirect() перенаправляет на другой сайт, принимает url
# функция abort() обрабатывает ошибки,принимает код ошибки
# функция render_template() создает шаблон html c параметрами
# функция url_for() создает URL по имени функции и переданным параметрам
# функция flash создает всплывающее сообщение
# глобальный словарь session позволяет передавать данные между запросами в 1 сессии
from flask import redirect, abort, render_template, session, url_for, flash
# unit for work with web form
from Forms import NameForm
from datetime import datetime


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
