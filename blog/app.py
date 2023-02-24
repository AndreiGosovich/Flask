from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello web!"


@app.route("/user/")
def read_user():
    name = request.args.get("name")
    surname = request.args.get("surname")
    return f"Hello {name or '[no name]'} {surname or '[no surname]'}!"