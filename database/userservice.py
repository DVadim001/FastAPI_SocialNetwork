from database.models import User
from database import get_db


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users


# Получить определённого пользователя
def get_exact_user_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        return exact_user.user_id
    else:
        return 'Такого пользователя нет'


# Регистрация пользователя
def register_user_db(name, surname, phone_number, email, city, birthday, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number)
    if checker:
        return checker.user_id
    else:
        new_user = User(name=name,
                        surname=surname,
                        phone_number=phone_number,
                        email=email,
                        city=city,
                        birthday=birthday,
                        password=password)
        db.add(new_user)
        db.commit()
        return new_user.id


# Логин пользователя
def login_user_db(phone_number, password):
    db = next(get_db())
    login = db.query(User).filter_by(phone_number=phone_number, password=password).first()
    if login:
        return f'Вход выполнен успешно для пользователя {login.user_id}'
    else:
        return 'Неверный номер телефона или пароль'


# Удаление пользователя
def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return f'Пользователь с ID {user_id} удален'
    else:
        return 'Пользователь не найден'


# Изменение данных пользователя
def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())
    exec_user = get_exact_user_db(user_id)
    if exec_user:
        if edit_info == 'name':
            exec_user.name = new_info
        elif edit_info == 'surname':
            exec_user.surname = new_info

        db.commit()
        return 'Данные Успешно изменены!'
    else:
        return "Пользователь не найден."


# Добавить фото профиля
def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())

    exec_user = get_exact_user_db(user_id)
    if exec_user:
        exec_user.profile_photo = photo_path
        db.commit()
        return "Успешно"
    else:
        return "Пользователь не найден."


# Удаление фото профиля
def delete_profile_photo_db(user_id):
    db = next(get_db())
    exec_user = get_exact_user_db(user_id)
    if exec_user:
        exec_user.profile_photo = 'None'
        db.commit()
        return "Фото профиля удалено"
    else:
        return "Пользователь не найден."
