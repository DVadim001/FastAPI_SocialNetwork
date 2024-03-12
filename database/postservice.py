from database.models import PostPhoto, UserPost
from database import get_db
from datetime import datetime

# Получить все публикации
def get_all_posts_db():
    db = next(get_db())
    all_posts = db.query(UserPost).all()
    return all_posts


# Получить оптеделённую публикацию
def get_exact_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        return exact_post.post_id
    else:
        return 'Такого поста нет'


# Добавить публикацию
def add_new_post_db(user_id, post_text):
    db = next(get_db())
    new_post = UserPost(user_id=user_id, post_text=post_text, publish_date=datetime.now())
    db.add(new_post)
    db.commit()
    return f'Успешно добавлен {new_post.post_id}'


# Изменить текст к публикации
def edit_post_text_db(post_id, new_text):
    db = next(get_db())
    exac_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exac_post:
        exac_post.post_text = new_text
        db.commit()
        return "Текст к публикации изменён"
    else:
        return 'Пост не найден'


# Удалить публикацию
def delete_post_db(post_id):
    db = next(get_db())
    post = db.query(UserPost).filter_by(post_id=post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return f'Пост с ID {post_id} удален'
    else:
        return 'Пост не найден'


# Добавить лайк к публикации
def like_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.likes += 1
        db.commit()
        return "Лайк добавлен"
    else:
        return 'Пост не найден'

# Удалить лайк из публикации
def unlike_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.likes -= 1
        db.commit()
        return "Лайк снят"
    else:
        return 'Пост не найден'
