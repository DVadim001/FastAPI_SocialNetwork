from fastapi import APIRouter, UploadFile
from database.postservice import (get_all_posts_db,
                                  get_exact_post_db,
                                  add_new_post_db,
                                  edit_post_text_db,
                                  delete_post_db,
                                  add_like_post_db,
                                  unlike_post_db,
                                  upload_post_photo_db,
                                  delete_post_photo_db,
                                  all_photos_db)
from posts import PublicPostValidator, EditPostValidator

post_router = APIRouter(prefix='/posts', tags=['Работа с публикациями'])


# Загружаем наши посты
@post_router.post('/public_post')
async def publish_post(data: PublicPostValidator):
    result = add_new_post_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Пост не найден"}


# Запрос на удадение поста
@post_router.delete('/delete_post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': "Пост не найден"}


# Получить все публикации
@post_router.get('/all')
async def get_all():
    result = get_all_posts_db()
    return {'message': result}


# Получить определённую публикацию
@post_router.get('/post')
async def get_post(post_id):
    result = get_exact_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': "Такого поста нет."}


# Загрузить фото к определённому посту
@post_router.post('/add-photo')
async def add_photo(post_id: int, photo_path: UploadFile = None):
    with open(f'media/{photo_path.filename}', 'wb') as file:
        user_photo = await photo_path.read()
        file.write(user_photo)
    result = upload_post_photo_db(post_id, f'/madia/{photo_path.file}')
    if result:
        return {'message': result}
    else:
        return {'message': "Ошибка при загрузке изображения"}


# Изменить текст определённой публикации
@post_router.put('/edit')
async def edit_post(data: EditPostValidator):
    result = edit_post_text_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Ошибка при изменении"}


# Запрос на получение всех фотографий
@post_router.get('/all-photo')
async def all_photos():
    result = all_photos_db()
    if result:
        return {'message': result}
    else:
        return {'message': "Ошибка при получении"}


# Удалить публикацию
@post_router.delete('/delete-post')
async def delete_post(post_id):
    return delete_post_db(post_id)


# Добавить лайк к публикации
@post_router.post('/add-like')
async def add_like(post_id):
    return add_like_post_db(post_id)


# Удалить лайк из публикации
@post_router.delete('/add-unlike')
async def unlike(post_id):
    return unlike_post_db(post_id)


# Удаление фотографии определённого поста
@post_router.delete('/delete-photo')
async def delete_photo(post_id):
    return delete_post_photo_db(post_id)
