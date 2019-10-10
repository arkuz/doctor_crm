from flask import render_template, request, session, redirect

import webapp.helpers.data_mos_ru_helpers as dms_helper
import webapp.parsing.get_information
import webapp.parsing.get_page
import webapp.helpers.db.doctors_helpers as db_user
from webapp.helpers.sendgrid_helpers import send_reg_email_to_user


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
            if db_user.registration(email, password):
                send_reg_email_to_user(email, password)
                session['username'] = email
                return redirect('moscow_clinic_list')
            error_msg = f'Пользователь с почтовым ящиком {email} уже существует'
        else:
            if db_user.login(email, password):
                session['username'] = email
                return redirect('moscow_clinic_list')
            error_msg = 'Неверный логин или пароль'

    return render_template('registration.html',
                           error_msg=error_msg,
                           title=title)


def logout():
    session.pop('username', None)
    return redirect('/')


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
