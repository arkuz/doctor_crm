from flask import Flask
from flask_login import LoginManager

from webapp.model import db
import webapp.page_handlers as page_handlers
import webapp.endpoint_handlers as endpoint_handlers
from webapp.doctor.models import Doctor

from webapp.doctor.views import blueprint as doctor_blueprint
from webapp.patient.views import blueprint as patient_blueprint
from webapp.case.views import blueprint as case_blueprint


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
    app.register_blueprint(patient_blueprint)

    # pages
    '''
    app.add_url_rule('/', 'index', page_handlers.index)
    app.add_url_rule('/login', 'login', page_handlers.login)
    app.add_url_rule('/process_login', 'process_login', page_handlers.process_login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', page_handlers.logout)
    '''
    app.add_url_rule('/admin', 'admin', page_handlers.admin)
    app.add_url_rule('/moscow_clinic_list', 'moscow_clinic_list', page_handlers.moscow_clinic_list)
    app.add_url_rule('/parse_and_show', 'parse_and_show', page_handlers.parse_and_show)

    # endpoints
    api_prefix = '/api/v1.0'
    app.add_url_rule(f'{api_prefix}/doctors/',
                     view_func=endpoint_handlers.get_doctors,
                     methods=['GET'])

    app.add_url_rule(f'{api_prefix}/doctors/<int:doctor_id>',
                     view_func=endpoint_handlers.get_doctor_by_id,
                     methods=['GET'])

    return app
