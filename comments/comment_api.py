from fastapi import APIRouter
from database.commentservice import (add_comment_db,
                                     delete_comment_db,
                                     change_comment_db,
                                     get_post_comments_db)
from comments import PublicPostValidator, EditPostValidator

comment_router = APIRouter(prefix='/comments', tags=['Работа с комментариями'])


# Добавить комментарий
@comment_router.post('/add-comment')
async def add_comment(data: PublicPostValidator):
    result = add_comment_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Комментарий не найден"}


# Удаление комментариев
@comment_router.delete('/delete-comment')
async def delete_comment(post_id, comment_id):
    result = delete_comment_db(post_id, comment_id)
    if result:
        return {'message': result}
    else:
        return {'message': "Комментарий не найден"}


# Изменить определённый комментарий
@comment_router.post('/edit-comment')
async def change_comment(data: EditPostValidator):
    result = change_comment_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Комментарий не найден"}


# Получить все комменты определённого поста
@comment_router.get('/comment')
async def get_comment(post_id):
    return get_post_comments_db(post_id)
