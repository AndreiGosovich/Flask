from flask import json, jsonify
from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.permissions.article import ArticlePermission
from blog.schemas import ArticleSchema
from blog.models.database import db
from blog.models import Article

from combojsonapi.event.resource import EventsResource


class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {"count": Article.query.count()}

    def event_get_all_articles(self, _permission_user=None):
        print('Article.query.all() >>>>>> ', Article.query.all())
        ret_val = jsonify(articles=ArticleSchema().dump(Article.query.all(), many=True))
        print(ret_val)
        return ret_val


class ArticleList(ResourceList):
    events = ArticleListEvents
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
        "permission_patch": [ArticlePermission],
    }
