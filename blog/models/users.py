from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255))
    is_staff = Column(Boolean, nullable=False, default=False)
    full_name = Column(String(255))
    address = Column(String(255), default="", server_default="")

    def __repr__(self):
        return self.username
