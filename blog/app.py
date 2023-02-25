from flask import Flask, render_template, request
from blog.views.users import users_app
from blog.views.articles import articles_app

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/")
def read_user():
    name = request.args.get("name")
    surname = request.args.get("surname")
    return f"Hello {name or '[no name]'} {surname or '[no surname]'}!"
