from flask import Flask, render_template, request
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.config["SECRET_KEY"] = "abcdefg123456"
app.register_blueprint(auth_app, url_prefix="/auth")
login_manager.init_app(app)


@app.route("/", endpoint="mainpage")
def index():
    return render_template("index.html")


# @app.route("/user/")
# def read_user():
#     name = request.args.get("name")
#     surname = request.args.get("surname")
#     return f"Hello {name or '[no name]'} {surname or '[no surname]'}!"
