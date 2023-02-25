from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.views.users import USERS

articles_app = Blueprint("articles_app", __name__)

ARTICLES = {
    1: {
        "title": "Как правильно пользоваться Flask",
        "text": "Flask - это легковесный фреймворк для веб-приложений на языке Python. Он позволяет быстро и просто "
                "создавать веб-приложения, которые могут быть использованы в различных областях. В этой статье мы "
                "рассмотрим основы работы с Flask и научимся создавать простые веб-приложения.",
        "author_id": 1,
    },
    2: {
            "title": "Как создать дизайн сайта в Bootstrap",
            "text": "Bootstrap - это один из самых популярных фреймворков для создания дизайна сайтов. Он предлагает "
                    "множество готовых компонентов и классов, которые позволяют быстро и просто создавать красивые и "
                    "современные сайты. В этой статье мы рассмотрим основы работы с Bootstrap и научимся создавать "
                    "современные сайты с помощью этого фреймворка.",
            "author_id": 2,
        },
    3: {
            "title": "Как работать с базами данных в Flask",
            "text": "Базы данных - это очень важная часть любого веб-приложения. Они позволяют хранить и обрабатывать "
                    "большие объемы данных, которые могут быть использованы в различных областях. В этой статье мы "
                    "рассмотрим основы работы с базами данных в Flask и научимся создавать простые приложения, которые "
                    "будут использовать базы данных.",
            "author_id": 3,
        }
}


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id: int):
    try:
        article = ARTICLES[article_id]
        article_title = article.get('title')
        article_text = article.get('text')
        article_author = USERS[article.get('author_id')]
    except KeyError:
        raise NotFound(f"Article id #{article_id} doesn't exist!")
    return render_template('articles/details.html', article_tilte=article_title, article_text=article_text,
                           article_author=article_author, article_id=article_id)
