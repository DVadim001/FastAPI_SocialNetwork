# from fastapi import APIRouter
# from database.postservice import (get_all_posts_db,
#                                   get_exact_post_db,
#                                   add_new_post_db,
#                                   edit_post_text_db,
#                                   delete_post_db,
#                                   # like_post_db,
#                                   unlike_post_db,
#                                   upload_post_photo_db,
#                                   delete_post_photo_db,
#                                   all_photos_db)
#
# post_router = APIRouter(prefix='/posts', tags=['Работа с публикациями'])
#
#
# # Получить все публикации
# @post_router.get('/all')
# async def get_posts():
#     return get_all_posts_db()
#
#
# # Получить определённую публикацию
# @post_router.get('/post')
# async def get_post(post_id):
#     return get_exact_post_db(post_id)
#
#
# # Добавить публикацию
# @post_router.post('/add-post')
# async def test3():
#     pass
#
#
# # Изменить текст к публикации
# @post_router.post('/')
# async def test4():
#     pass
#
#
# # Удалить публикацию
# @post_router.delete('/')
# async def test4():
#     pass
#
#
# # Добавить лайк к публикации
# @post_router.post('/')
# async def test5():
#     pass
#
#
# # Удалить лайк из публикации
# @post_router.delete('/')
# async def test6():
#     pass
#
#
# # Загрузить фото к определённому посту
# @post_router.post('/')
# async def test7():
#     pass
#
#
# # Удаление фотографии определённого поста
# @post_router.delete('/')
# async def test8():
#     pass
#
#
# # Запрос на получение всех фотографий
# @post_router.get('/')
# async def test9():
#     pass
