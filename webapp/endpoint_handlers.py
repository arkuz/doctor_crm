from flask import jsonify
from flask_login import current_user

from webapp.model import Doctor


def get_doctors():
    if current_user.is_authenticated:
        doctors_list = [doc.json_dump() for doc in Doctor.query.all()]
        return jsonify({'doctors': doctors_list})
    return 'Ошибка, вы не авторизованы!'


def get_doctor_by_id(doctor_id):
    if current_user.is_authenticated:
        doctor = [doc.json_dump() for doc in Doctor.query.filter(Doctor.id == doctor_id)]
        return jsonify({'doctors': doctor})
    return 'Ошибка, вы не авторизованы!'
