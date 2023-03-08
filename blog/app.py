from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app
import os
from flask_migrate import Migrate
from blog.security import flask_bcrypt
from blog.views.authors import authors_app


def create_app() -> Flask:
    app = Flask(__name__)

    cfg_name = os.environ.get("ProductionConfig") or "DevConfig"
    app.config.from_object(f"blog.configs.{cfg_name}")

    register_extentions(app)
    register_blueprints(app)

    @app.route("/", endpoint="mainpage")
    def index():
        return render_template("index.html")

    return app


def register_extentions(app):
    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)
    flask_bcrypt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(auth_app, url_prefix="/auth")
    app.register_blueprint(authors_app, url_prefix="/authors")
