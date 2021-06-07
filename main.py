from flask import Flask, request
import sqlalchemy
import sqlite3

import view

app = Flask(__name__)
#naive realisation handlers of pages

@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    print(app.url_map)
    return f"<h1>Hello {user_agent}</h1>"


@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello {name}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
