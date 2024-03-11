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


# регистрация пользователя
def register_user_db(name, surname, phone_number, city, birthday, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number)
    if checker:
        return checker.user_id
    else:
        new_user = User(name=name, surname=surname, phone_number=phone_number,
                        city=city, birthday=birthday, password=password)
        db.add(new_user)
        db.commit()
        return new_user.id
