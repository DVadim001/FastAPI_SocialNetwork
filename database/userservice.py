from database.models import User
from database import get_db
from database.security import create_access_token


# Регистрация пользователя
def register_user_db(username, surname, phone_number, city, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return 'Данный номер телефона уже есть в базе'
    else:
        new_user = User(username=username, surname=surname, phone_number=phone_number, city=city, password=password)
        db.add(new_user)
        db.commit()
        return f'Успешно зарегистрирован: {new_user.user_id}'


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    get_all_users = db.query(User).all()
    return get_all_users


# Получить определенного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(user_id=user_id).first()
    if checker:
        return f'Пользователь найден: {checker.user_id}'
    else:
        return 'Пользователь не обнаружен'


# Логин
def login_user_db(username, password):
    db = next(get_db())
    login = db.query(User).filter_by(username=username, password=password).first()
    if login:
        token_data = {"user_id": login.user_id}
        access_token_data = create_access_token(token_data)
        return {"access_token": access_token_data, "token_type": "Bearer", "status": "Success"}
    else:
        return 'Неверный номер телефона или пароль'


# Изменения данных пользователя
def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        if edit_info == 'username':
            exact_user.username = new_info
        elif edit_info == 'surname':
            exact_user.surname = new_info
        db.commit()
        return 'Данные успешно изменены.'
    else:
        return 'Пользователь не найден.'


# Добавить фото профиля
def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())
    exact_user = get_exact_user_db(user_id)
    if exact_user:
        exact_user.profile_photo = photo_path
        db.commit()
        return 'Успешно!'
    else:
        return 'Пользователь не найден'


# Удаления фото профиля
def delete_profile_photo_db(user_id):
    db = next(get_db())
    exact_user = get_exact_user_db(user_id)
    if exact_user:
        exact_user.profile_photo = 'None'
        db.commit()
        return 'Фото профиля удалено'
    else:
        return 'Пользователь не найден'


#  Удаления пользователя
def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return f'Пользователь с ID {user_id} удален'
    else:
        return 'Пользователь не найден'
