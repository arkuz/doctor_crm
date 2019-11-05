from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from webapp.doctor.forms import LoginForm
from webapp.helpers.sendgrid_helpers import send_reg_email_to_user
from webapp.doctor.models import db, Doctor, Timing
from flask import Blueprint
from flask.views import MethodView
from webapp.common.views import AuthRequiredMethodView


blueprint = Blueprint('doctor', __name__)


class DoctorIndexView(MethodView):
    def get(self):
        return render_template('doctor/index.html')


class DoctorLoginView(MethodView):
    def get(self):
        login_form = LoginForm()
        title = 'Авторизация'
        return render_template('doctor/login.html',
                               title=title,
                               form=login_form)


class DoctorsLoginProcessView(MethodView):
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        reg = request.form.get('reg')

        if not email or not password:
            flash('Заполните логин / пароль')
            return redirect(url_for('doctor.login'))

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
                return redirect(url_for('doctor.index'))

            flash('Пользователь с таким email уже существует')
            return redirect(url_for('doctor.login'))

        if doctor and doctor.check_password(password):
            login_user(doctor)
            flash('Вы успешно вошли на сайт')
            return redirect(url_for('doctor.index'))

        flash('Неверный логин или пароль')

        return redirect(url_for('doctor.login'))


class DoctorLogoutView(AuthRequiredMethodView):
    def get(self):
        logout_user()
        return redirect(url_for('doctor.login'))


class DoctorTimingView(AuthRequiredMethodView):
    def get(self):
        title = 'Личный кабинет'
        timing = None
        if current_user.is_doctor:
            timing = Timing.query.filter(Timing.doctor_id == current_user.id)
        return render_template('doctor/timing.html',
                               title=title,
                               timing=timing)


blueprint.add_url_rule('/', view_func=DoctorIndexView.as_view('index'))
blueprint.add_url_rule('/login', view_func=DoctorLoginView.as_view('login'))
blueprint.add_url_rule('/process_login', view_func=DoctorsLoginProcessView.as_view('process_login'))
blueprint.add_url_rule('/logout', view_func=DoctorLogoutView.as_view('logout'))

blueprint.add_url_rule('/timing', view_func=DoctorTimingView.as_view('timing'))
