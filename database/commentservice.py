from database.models import PostComments
from datetime import datetime
from database import get_db


# Опубликовать комментарий
def add_comment_db(post_id, comment_text, user_id):
    db = next(get_db())
    new_comment = PostComments(post_id=post_id, comment_text=comment_text, user_id=user_id, publish_date=datetime.now())
    if new_comment:
        db.add(new_comment)
        db.commit()
        return "Комментарий успешно добавлен."
    else:
        return "Запрашиваемого поста нет."


# Удаление комментариев
def delete_comment_db(post_id, comment_id):
    db = next(get_db())
    exac_comment = db.query(PostComments).filter_by(post_id=post_id, comment_id=comment_id).first()
    if exac_comment:
        db.delete(exac_comment)
        db.commit()
        return "Успешно удалён"
    else:
        return "Запрашиваемого комментария нет"


# Изменить определённый комментарий
def change_comment_db(post_id, comment_id, change_text):
    db = next(get_db())
    exact_comment = db.query(PostComments).filter_by(post_id=post_id, comment_id=comment_id).first()
    if exact_comment:
        if comment_id == 'text_comment':
            exact_comment.name = change_text
        db.commit()
        return 'Комментарий успешно изменён'
    else:
        return "Комментарий не найден."


# Получить все комменты определённого поста
def get_post_comment(post_id):
    db = next(get_db())
    post_comment = db.query(PostComments).filter_by(post_id=post_id).all()
    if post_comment:
        return post_comment
    else:
        return "Комментарии не найдены"
