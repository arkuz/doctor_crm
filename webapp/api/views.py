from flask import jsonify, Blueprint
from flask.views import MethodView
from flask_login import current_user

from webapp.doctor.models import Doctor


blueprint = Blueprint('api', __name__, url_prefix='/api/v1.0')


class DoctorsListView(MethodView):
    def get(self):
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


blueprint.add_url_rule('/doctors', view_func=DoctorsListView.as_view('list_doctors'))
