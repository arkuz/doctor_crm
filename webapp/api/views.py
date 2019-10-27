from flask import jsonify, current_app
from flask_login import current_user
from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from webapp.doctor.models import Doctor


blueprint = Blueprint('api', __name__, url_prefix='/api/v1.0')


@blueprint.route('/doctors')
def get_doctors():
    if current_user.is_authenticated:
        doctors_list = [doc.json_dump() for doc in Doctor.query.all()]
        return jsonify({'doctors': doctors_list})
    return 'Ошибка, вы не авторизованы!'


@blueprint.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor_by_id(doctor_id):
    if current_user.is_authenticated:
        doctor = [doc.json_dump() for doc in Doctor.query.filter(Doctor.id == doctor_id)]
        return jsonify({'doctors': doctor})
    return 'Ошибка, вы не авторизованы!'


@blueprint.route('/db_view')
def db_view():
    if current_user.is_authenticated:
        admin_app = Admin(current_app)
        db = current_app
        admin_view = admin_app.add_view(ModelView(Doctor, db.session))
        return admin_view
    return 'Ошибка, вы не авторизованы!'
