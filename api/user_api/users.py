from fastapi import APIRouter
from database.userservice import (register_user_db,
                                  get_all_users_db,
                                  get_exact_user_db,
                                  login_user_db,
                                  delete_user_db,
                                  edit_user_info_db,
                                  upload_profile_photo_db)

user_router = APIRouter(prefix='/users', tags=['Работа с пользователями'])


# Регистрация пользователя
@user_router.post('/register')
async def register(name: str, surname: str, phone_number: int, email: str, city: int, birthday, password: str):
    register_user = register_user_db(name, surname, phone_number, email, city, birthday, password)
    return f'Вы успешно зарегистрировались как {register_user}'


# Получить всех пользователей
@user_router.get('/all')
async def get_users():
    return get_all_users_db()


# Получить определённого пользователя
@user_router.get('/user')
async def get_user(user_id: int):
    return get_exact_user_db(user_id)


# Логин пользователя
@user_router.get('/')
async def test3():
    pass


# Удаление пользователя
@user_router.delete('/')
async def test4():
    pass


# Изменение данных пользователя
@user_router.post('/')
async def test5():
    pass


# Добавить фото профиля
@user_router.post('/')
async def test():
    pass


# Удаление фото профиля
@user_router.delete('/')
async def test6():
    pass
