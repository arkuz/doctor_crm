import sys

from webapp import create_app
from webapp.db import db
from webapp.doctor.models import Doctor


app = create_app()

doctors = [
    {
        'email': 'admin@doc.ru',
        'password': '123',
        'surname': 'Админов Админ Админович',
        'specialization': 'Админ',
        'address': 'село Админское',
        'is_admin': 1,
    },
    {
        'email': 'doc1@doc.ru',
        'password': '123',
        'surname': 'Борисов Петр Михайлович',
        'specialization': 'Хирург',
        'address': 'Москва, Кутузовский проспект 223',
        'is_admin': 0,
    },
    {
        'email': 'doc2@doc.ru',
        'password': '123',
        'surname': 'Иванов Сергей Петрович',
        'specialization': 'Терапевт',
        'address': 'Москва, ул. Ленина 22',
        'is_admin': 0,
    },
    {
        'email': 'doc3@doc.ru',
        'password': '123',
        'surname': 'Новикова Элла Дмитриевна',
        'specialization': 'Невролог',
        'address': 'Москва, ул. Ульянова 13/6',
        'is_admin': 0,
    },
]

with app.app_context():

    for doctor in doctors:
        if Doctor.query.filter(Doctor.email == doctor['email']).count():
            print(f'Пользователь с email {doctor["email"]} уже есть в БД')  # noqa
            continue

        new_Doctor = Doctor(
            email=doctor['email'],
            surname=doctor['surname'],
            specialization=doctor['specialization'],
            address=doctor['address'],
            is_admin=doctor['is_admin'],
        )
        new_Doctor.set_password(doctor['password'])
        db.session.add(new_Doctor)
        db.session.commit()
        print('Doctor with id {} added'.format(new_Doctor.id)) # noqa

print('Test doctors added') # noqa
sys.exit(0)
