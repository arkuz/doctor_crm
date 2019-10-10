import hashlib
from webapp.model import db, Doctor
from webapp.config import PASSWORD_SALT


def is_user_exist(email):
    return Doctor.query.filter(Doctor.email == email).count()


def registration(email, password):
    reg_success = False
    if not is_user_exist(email):
        user = Doctor(email=email,
                      password=get_password_hash(password))
        db.session.add(user)
        db.session.commit()
        reg_success = True
    return reg_success


def login(email, password):
    return Doctor.query.filter(Doctor.email == email).filter(Doctor.password == get_password_hash(password)).count()


def get_password_hash(password):
    password = password.strip()
    password_hash = hashlib.sha512()
    password_hash.update(f'{PASSWORD_SALT}{password}'.encode('utf-8'))
    return password_hash.hexdigest()
