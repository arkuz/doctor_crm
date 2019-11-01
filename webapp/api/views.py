from flask import jsonify, Blueprint


from webapp.doctor.models import Doctor
from webapp.common.views import AuthRequiredMethodView


blueprint = Blueprint('api', __name__, url_prefix='/api/v1.0')


class DoctorsListView(AuthRequiredMethodView):
    def get(self):
        doctors_list = [doc.json_dump() for doc in Doctor.query.all()]
        return jsonify({'doctors': doctors_list})


class DoctorListView(AuthRequiredMethodView):
    def get(self, doctor_id):
        doctor = [doc.json_dump() for doc in Doctor.query.filter(Doctor.id == doctor_id)]
        return jsonify({'doctors': doctor})


blueprint.add_url_rule('/doctors', view_func=DoctorsListView.as_view('list_doctors'))
blueprint.add_url_rule('/doctors/<int:doctor_id>', view_func=DoctorListView.as_view('list_doctor'))
