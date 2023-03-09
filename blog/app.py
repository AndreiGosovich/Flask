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
    register_commands(app)

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


def register_commands(app):
    @app.cli.command("create-admin")
    def create_admin():
        """
        Run in your terminal:
        ➜ flask create-admin
        > created admin: <User #1 'admin'>
        """
        from blog.models import User

        admin = User(username="admin", is_staff=True, first_name="Админ", last_name="Админыч", email="фвьшт@q.q")
        admin.password = os.environ.get("ADMIN_PASSWORD") or "admin"

        db.session.add(admin)
        db.session.commit()

        print("created admin:", admin)

    @app.cli.command("create-users")
    def create_users():
        """
        Run in your terminal:
        flask create-users
        """
        from blog.models import User

        ivan = User(username="ivan", first_name="Иван", last_name="Иванов", email="ivan@q.q",
                    password="ivan", id=8)
        peter = User(username="peter", first_name="Петр", last_name="Петров", email="peter@q.q",
                     password="peter", id=9)
        sidor = User(username="sidor", first_name="Сидор", last_name="Сидоров", email="sidor@q.q",
                     password="sidor", id=10)

        db.session.add(ivan)
        db.session.add(peter)
        db.session.add(sidor)
        db.session.commit()

        print("done! created users:", ivan, peter, sidor)

    @app.cli.command("create-articles")
    def create_articles():
        """
        Run in your terminal:
        flask create-articles
        """
        from blog.models import Article
        first = Article(
            title="Как правильно пользоваться Flask",
            author_id=8,
            text="Flask - это легковесный фреймворк для веб-приложений на языке Python. Он позволяет быстро и просто "
                 "создавать веб-приложения, которые могут быть использованы в различных областях. В этой статье мы "
                 "рассмотрим основы работы с Flask и научимся создавать простые веб-приложения.")

        second = Article(
            title="Как создать дизайн сайта в Bootstrap",
            author_id=9,
            text="Bootstrap - это один из самых популярных фреймворков для создания дизайна сайтов. Он предлагает "
                 "множество готовых компонентов и классов, которые позволяют быстро и просто создавать красивые и "
                 "современные сайты. В этой статье мы рассмотрим основы работы с Bootstrap и научимся создавать "
                 "современные сайты с помощью этого фреймворка.")

        third = Article(
            title="Как работать с базами данных в Flask",
            author_id=10,
            text="Базы данных - это очень важная часть любого веб-приложения. Они позволяют хранить и обрабатывать "
                 "большие объемы данных, которые могут быть использованы в различных областях. В этой статье мы "
                 "рассмотрим основы работы с базами данных в Flask и научимся создавать простые приложения, которые "
                 "будут использовать базы данных.")

        db.session.add(first)
        db.session.add(second)
        db.session.add(third)
        db.session.commit()

        print("done! created articles:", first, second, third)

    @app.cli.command("create-tags")
    def create_tags():
        """
        Run in your terminal:
        ➜ flask create-tags
        """
        from blog.models import Tag
        for name in [
            "flask",
            "django",
            "python",
            "sqlalchemy",
            "news",
        ]:
            tag = Tag(name=name)
            db.session.add(tag)
        db.session.commit()
        print("created tags")
