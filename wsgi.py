from blog.app import app
from blog.models.database import db
from werkzeug.security import generate_password_hash

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    """
    from blog.models import User
    admin = User()
    admin.username = "admin"
    admin.is_staff = True
    admin.full_name = "admin"
    admin.email = "admin@q.q"
    admin.password = generate_password_hash("admin")
    ivan = User(username="ivan", full_name="Иванов Иван Иванович", email="ivan@q.q",
                password=generate_password_hash("ivan"))
    peter = User(username="peter", full_name="Петров Петр Петрович", email="peter@q.q",
                 password=generate_password_hash("peter"))
    sidor = User(username="sidor", full_name="Сидоров Сидор Сидорович", email="sidor@q.q",
                 password=generate_password_hash("sidor"))

    db.session.add(admin)
    db.session.add(ivan)
    db.session.add(peter)
    db.session.add(sidor)
    db.session.commit()

    print("done! created users:", admin, ivan, peter, sidor)


@app.cli.command("create-articles")
def create_users():
    """
    Run in your terminal:
    flask create-articles
    """
    from blog.models import Article
    first = Article(
        title="Как правильно пользоваться Flask",
        author_id=1,
        text="Flask - это легковесный фреймворк для веб-приложений на языке Python. Он позволяет быстро и просто "
             "создавать веб-приложения, которые могут быть использованы в различных областях. В этой статье мы "
             "рассмотрим основы работы с Flask и научимся создавать простые веб-приложения.")

    second = Article(
        title="Как создать дизайн сайта в Bootstrap",
        author_id=2,
        text="Bootstrap - это один из самых популярных фреймворков для создания дизайна сайтов. Он предлагает "
             "множество готовых компонентов и классов, которые позволяют быстро и просто создавать красивые и "
             "современные сайты. В этой статье мы рассмотрим основы работы с Bootstrap и научимся создавать "
             "современные сайты с помощью этого фреймворка.")

    third = Article(
        title="Как работать с базами данных в Flask",
        author_id=3,
        text="Базы данных - это очень важная часть любого веб-приложения. Они позволяют хранить и обрабатывать "
             "большие объемы данных, которые могут быть использованы в различных областях. В этой статье мы "
             "рассмотрим основы работы с базами данных в Flask и научимся создавать простые приложения, которые "
             "будут использовать базы данных.")

    db.session.add(first)
    db.session.add(second)
    db.session.add(third)
    db.session.commit()

    print("done! created articles:", first, second, third)