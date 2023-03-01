from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    text = Column(String, nullable=False)
    author_id = Column(Integer)

    def __repr__(self):
        return f"<Article #{self.id}: {self.title!r}>"
