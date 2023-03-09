from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, func
from sqlalchemy.orm import relationship

from blog.models.article_tag import article_tag_association_table
from blog.models.database import db


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, default="", server_default="")
    text = Column(Text, nullable=False, default="", server_default="")
    author_id = Column(Integer, ForeignKey("author.id", name="articles-author"))
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship("Author", back_populates="articles")

    tags = relationship(
        "Tag",
        secondary=article_tag_association_table,
        back_populates="articles",
    )

    def __repr__(self):
        return f"<Article #{self.id}: {self.title!r}>"
