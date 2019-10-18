from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required

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
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        reg = request.form.get('reg')

        if not email or not password:
            flash('Заполните логин / пароль')
            return redirect(url_for('login'))

        doctor = Doctor.query.filter(Doctor.email == email).first()
        if reg:
            if not doctor:
                doctor = Doctor(email=email, is_admin=0)
                doctor.set_password(password)
                db.session.add(doctor)
                db.session.commit()
                send_reg_email_to_user(email, password)
                login_user(doctor)
                flash('Вы успешно зарегистрировались')
                return redirect(url_for('index'))

            flash('Пользователь с таким email уже существует')
            return redirect(url_for('login'))

        if doctor and doctor.check_password(password):
            login_user(doctor)
            flash('Вы успешно вошли на сайт')
            return redirect(url_for('index'))

        flash('Неверный логин или пароль')

    return redirect(url_for('login'))


def logout():
    logout_user()
    return redirect(url_for('login'))


@login_required
def admin():
    if current_user.is_administrator:
        return 'Админ привет!'
    return 'Вы не админ!'


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
