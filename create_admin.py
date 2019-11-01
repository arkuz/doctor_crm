from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db
from webapp.doctor.models import Doctor


app = create_app()

with app.app_context():
    email = input('Введите email пользователя: ')

    if Doctor.query.filter(Doctor.email == email).count():
        print('Такой пользователь уже есть') # noqa
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        print('Пароли не совпадают') # noqa
        sys.exit(0)

    new_Doctor = Doctor(email=email, role='admin')
    new_Doctor.set_password(password)

    db.session.add(new_Doctor)
    db.session.commit()
    print('Doctor with id {} added'.format(new_Doctor.id)) # noqa
