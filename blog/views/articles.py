from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import Article, User

articles_app = Blueprint("articles_app", __name__)


@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@articles_app.route("/<int:article_id>/", endpoint="details")
@login_required
def article_details(article_id: int):
    article = Article.query.filter_by(id=article_id).one_or_none()

    if article is None:
        raise NotFound(f"Article id #{article_id} doesn't exist!")

    user = User.query.filter_by(id=article.author_id).one_or_none()
    article_author = 'none'
    if user is not None:
        article_author = user.full_name

    return render_template('articles/details.html', article=article, article_author=article_author)
