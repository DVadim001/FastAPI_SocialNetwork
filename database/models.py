from sqlalchemy import Column, DateTime, String, Date, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from database import Base


# Таблице пользователей
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True)
    city = Column(String)
    birthday = Column(Date)
    profile_photo = Column(String)
    reg_date = Column(DateTime)
    password = Column(String)


# Таблица публикаций
class UserPost(Base):
    __tablename__ = "user_posts"
    post_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    post_text = Column(Text)
    likes = Column(Integer, default=0)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


# Таблица фотографий, добавление фото к определённому посту
class PostPhoto(Base):
    __tablename__ = "post_photos"
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    photo_path = Column(String)

    post_fk = relationship(UserPost, lazy='subquery')


# Таблица комментариев
class PostComments(Base):
    __tablename__ = "post_comments"
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))

    comment_text = Column(Text)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')
