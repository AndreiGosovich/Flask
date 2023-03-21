import requests as requests
from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.forms.articles import CreateArticleForm
from blog.models import Article, Author, Tag
from blog.models.database import db

articles_app = Blueprint("articles_app", __name__)


@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@articles_app.route("/list_api/", endpoint="list_api")
def articles_list():
    # articles = Article.query.all()
    articles = requests.get('http://127.0.0.1:5000/api/articles/event_get_all_articles/').json()
    return render_template("articles/list_api.html", articles=articles)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id: int):
    article = Article.query.filter_by(id=article_id).options(
        joinedload(Article.tags)  # подгружаем связанные теги!
    ).one_or_none()

    if article is None:
        raise NotFound(f"Article id #{article_id} doesn't exist!")

    return render_template('articles/details.html', article=article)


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    # добавляем доступные теги в форму
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), text=form.text.data)
        if current_user.author:
            # use existing author if present
            article.author = current_user.author
        else:
            # otherwise create author record
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author

        if form.tags.data:  # если в форму были переданы теги (были выбраны)
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)  # добавляем выбранные теги к статье

        db.session.add(article)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles_app.details", article_id=article.id))

    return render_template("articles/create.html", form=form, error=error)


@articles_app.route("/tags/", endpoint="tags")
def tags_list():
    tags = Tag.query.all()
    return render_template("articles/tags.html", tags=tags)


@articles_app.route("/tags/<int:tag_id>/", endpoint="tag_details")
def tag_details(tag_id: int):
    tag = Tag.query.filter_by(id=tag_id).options(
        joinedload(Tag.articles)  # подгружаем связанные теги!
    ).one_or_none()

    if tag is None:
        raise NotFound(f"Tag id #{tag_id} doesn't exist!")

    return render_template('articles/tag_details.html', tag=tag)
