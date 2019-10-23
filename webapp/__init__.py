from flask import Flask
from flask_login import LoginManager

from webapp.model import db
import webapp.page_handlers as page_handlers
import webapp.endpoint_handlers as endpoint_handlers
from webapp.doctor.models import Doctor

from webapp.doctor.views import blueprint as doctor_blueprint
from webapp.patient.views import blueprint as patient_blueprint
from webapp.case.views import blueprint as case_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.clinic.views import blueprint as clinic_blueprint
from webapp.api.views import blueprint as api_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = app.config['SESSION_SECRET_KEY']
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'doctor.login'

    @login_manager.user_loader
    def load_user(doctor_id):
        return db.session.query(Doctor).get(doctor_id)

    app.register_blueprint(doctor_blueprint)
    app.register_blueprint(patient_blueprint)
    app.register_blueprint(case_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(clinic_blueprint)
    app.register_blueprint(api_blueprint)

    return app
