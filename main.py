from flask import Flask, request, make_response, redirect, abort
import sqlalchemy
import sqlite3

# секция комментариев
# функция redirect() перенаправляет на другой сайт, принимает url
#функция abort() обрабатывает ошибки,принимает код ошибки
import view

app = Flask(__name__)


# naive realisation handlers of pages

@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    print(app.url_map)

    return f"<h1>Hello {user_agent}</h1>"


@app.route("/user/<name>")
def user(name):
    if name == "Nik":
        abort(400)
    else:
        return f"<h1>Hello {name}</h1>"


@app.route("/bad/")
def bad():
    return redirect("http://ya.ru")


if __name__ == '__main__':
    app.run(debug=True)
