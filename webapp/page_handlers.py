from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user

import webapp.helpers.data_mos_ru_helpers as dms_helper
import webapp.parsing.get_information
import webapp.parsing.get_page
from webapp.forms import LoginForm
from webapp.helpers.sendgrid_helpers import send_reg_email_to_user
from webapp.model import db, Doctor


def index():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    else:
        return render_template('index.html')


def login():
    error_msg = ''
    login_form = LoginForm()
    title = 'Авторизация'
    return render_template('login.html',
                           title=title,
                           error_msg=error_msg,
                           form=login_form)


def process_login():
    error_msg = ''
    title = 'Doctor CRM'
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        reg = request.form.get('reg')

        if not email or not password:
            error_msg = 'Заполните логин / пароль'
            return redirect(url_for('login'))

        if reg:
            doctor = Doctor.query.filter(Doctor.email == email).first()
            if not doctor:
                doctor = Doctor(email=email)
                doctor.set_password(password)
                db.session.add(doctor)
                db.session.commit()
                send_reg_email_to_user(email, password)
                login_user(doctor)
                return redirect(url_for('index'))

        doctor = Doctor.query.filter(Doctor.email == email).first()
        if doctor and doctor.check_password(password):
            login_user(doctor)
            return redirect(url_for('index'))
        error_msg = 'Неверный логин или пароль'

    return render_template('login.html',
                           error_msg=error_msg,
                           title=title)


def logout():
    logout_user()
    return redirect(url_for('login'))


def moscow_clinic_list():
    if current_user.is_authenticated:
        title = 'Список больниц Москвы'
        clinics_list = dms_helper.fetch_clinics_list()
        extract_clinics_list = dms_helper.get_result_clinics_list(clinics_list)
        return render_template('moscow_clinic_list.html',
                               title=title,
                               clinics_list=extract_clinics_list,
                               )
    return 'Ошибка, вы не авторизованы!'


def parse_and_show():
    if current_user.is_authenticated:
        url = 'http://neuroreab.ru/centers/'
        title = f'Список больниц с {url}'
        clinics_list = webapp.parsing.get_information.get_data(webapp.parsing.get_page.get_html(url))
        return render_template('parse_and_show.html',
                               title=title,
                               clinics_list=clinics_list,
                               )
    return 'Ошибка, вы не авторизованы!'
