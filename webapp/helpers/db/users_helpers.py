import hashlib
from webapp.model import db, Users
from webapp.config import PASSWORD_SALT


def is_user_exist(email):
    return Users.query.filter(Users.email == email).count()


def registration(email, password):
    reg_success = False
    if not is_user_exist(email):
        user = Users(email=email,
                     password=get_password_hash(password))
        db.session.add(user)
        db.session.commit()
        reg_success = True
    return reg_success


def login(email, password):
    return Users.query.filter(Users.email == email).filter(Users.password == get_password_hash(password)).count()


def get_password_hash(password):
    password = password.strip()
    password_hash = hashlib.sha512()
    password_hash.update(f'{PASSWORD_SALT}{password}'.encode('utf-8'))
    return password_hash.hexdigest()
