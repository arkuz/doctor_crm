from flask import Flask

from webapp.model import db
import webapp.page_handlers as page_handlers


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = app.config['SESSION_SECRET_KEY']
    db.init_app(app)

    app.add_url_rule('/', 'index', page_handlers.index, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', page_handlers.logout)
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
