from fastapi import APIRouter
from database.commentservice import (add_comment_db,
                                     delete_comment_db,
                                     change_comment_db,
                                     get_post_comment)

comment_router = APIRouter(prefix='/comments', tags=['Работа с комментариями'])


# Опубликовать комментарий
@comment_router.post('/')
async def test1():
    pass


# Удаление комментариев
@comment_router.delete('/')
async def test2():
    pass


# Изменить определённый комментарий
@comment_router.post('/')
async def test3():
    pass


# Получить все комменты определённого поста
@comment_router.get('/comment')
async def get_comment(post_id):
    return get_post_comment(post_id)
