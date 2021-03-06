from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from webapp.db import db
from webapp.doctor.models import Doctor
from webapp.patient.models import Patient
from webapp.case.models import Case
from webapp.doctor.models import Timing

from webapp.doctor.views import blueprint as doctor_blueprint
from webapp.patient.views import blueprint as patient_blueprint
from webapp.case.views import blueprint as case_blueprint
from webapp.clinic.views import blueprint as clinic_blueprint
from webapp.api.views import blueprint as api_blueprint
from webapp.common.views import blueprint as common_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = app.config['SESSION_SECRET_KEY']
    db.init_app(app)
    admin = Admin(app)
    admin.add_view(ModelView(Doctor, db.session, endpoint='doctor_db'))
    admin.add_view(ModelView(Case, db.session, endpoint='case_db'))
    admin.add_view(ModelView(Timing, db.session, endpoint='timing_db'))
    admin.add_view(ModelView(Patient, db.session, endpoint='patient_db'))

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'doctor.login'

    @login_manager.user_loader
    def load_user(doctor_id):
        return db.session.query(Doctor).get(doctor_id)

    app.register_blueprint(doctor_blueprint)
    app.register_blueprint(patient_blueprint)
    app.register_blueprint(case_blueprint)
    app.register_blueprint(clinic_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(common_blueprint)

    return app
