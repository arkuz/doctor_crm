from flask import Flask, render_template, request, redirect, url_for, session

import webapp.helpers.data_mos_ru_helpers as dms_helper
import webapp.parsing.get_information
import webapp.parsing.get_page
from webapp.model import db
import webapp.helpers.db.users_helpers as db_user


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = app.config['SESSION_SECRET_KEY']
    db.init_app(app)

    @app.route('/', methods=['post', 'get'])
    def index():
        error_msg = ''
        title = 'Doctor CRM'
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            action = request.form.get('reg-login')

            if not email or not password:
                error_msg = 'Заполните логин / пароль'
                return render_template('registration.html',
                                       error_msg=error_msg,
                                       title=title)

            if action == 'reg':
                if not db_user.registration(email, password):
                    error_msg = f'Пользователь с ящиком {email} уже существует'
                else:
                    session['username'] = email
                    return redirect(url_for('moscow_clinic_list'))
            else:
                if db_user.login(email, password):
                    session['username'] = email
                    return redirect(url_for('moscow_clinic_list'))
                else:
                    error_msg = f'Неверный логин или пароль'

        return render_template('registration.html',
                               error_msg=error_msg,
                                       title=title)

    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return redirect(url_for('index'))

    @app.route('/moscow_clinic_list')
    def moscow_clinic_list():
        if 'username' in session:
            title = 'Список больниц Москвы'
            clinics_list = dms_helper.fetch_clinics_list()
            extract_clinics_list = dms_helper.get_result_clinics_list(clinics_list)
            return render_template('moscow_clinic_list.html',
                                   title=title,
                                   clinics_list=extract_clinics_list,
                                   )
        return 'Ошибка, вы не авторизованы!'

    @app.route('/parse_and_show')
    def parse_and_show():
        if 'username' in session:
            url = 'http://neuroreab.ru/centers/'
            title = f'Список больниц с {url}'
            clinics_list = webapp.parsing.get_information.get_data(webapp.parsing.get_page.get_html(url))
            return render_template('parse_and_show.html',
                                   title=title,
                                   clinics_list=clinics_list,
                                   )
        return 'Ошибка, вы не авторизованы!'

    return app
