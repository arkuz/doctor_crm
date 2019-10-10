from flask import jsonify

from webapp.model import Doctor


def get_doctors():
    doctors_list = [doc.json_dump() for doc in Doctor.query.all()]
    return jsonify({'doctors': doctors_list})


def get_doctor_by_id(doctor_id):
    doctor = [doc.json_dump() for doc in Doctor.query.filter(Doctor.doctor_id == doctor_id)]
    return jsonify({'doctors': doctor})
