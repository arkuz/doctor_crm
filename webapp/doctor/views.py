from datetime import datetime

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from webapp.doctor.forms import LoginForm, TimingAddForm, CasesAddForm
from webapp.helpers.sendgrid_helpers import send_reg_email_to_user
from webapp.doctor.models import db, Doctor, Timing
from webapp.case.models import Case
from flask import Blueprint
from flask.views import MethodView
from webapp.common.views import AuthRequiredMethodView


blueprint = Blueprint('doctor', __name__)


class DoctorIndexView(MethodView):
    def get(self):
        if current_user.is_anonymous:
            return redirect(url_for('doctor.login'))

        if current_user.is_doctor:
            return redirect(url_for('doctor.timing'))

        if current_user.is_registrator:
            return redirect(url_for('doctor.cases'))

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
                doctor = Doctor(email=email, role='doc', active=0)
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


class DoctorTimingAdd(AuthRequiredMethodView):
    def get(self):
        title = 'Добавить запись'
        timing_add_form = TimingAddForm()
        return render_template('doctor/timing_add.html',
                               title=title,
                               form=timing_add_form)

    def post(self):
        doctor_id = current_user.id
        day = datetime.strptime(request.form.get('day'), '%d.%m.%Y')
        hours_with = request.form.get('hours_with')
        minutes_with = request.form.get('minutes_with')
        hours_to = request.form.get('hours_to')
        minutes_to = request.form.get('minutes_to')
        timing = Timing(doctor_id=doctor_id,
                        day=day,
                        hours_with=hours_with,
                        minutes_with=minutes_with,
                        hours_to=hours_to,
                        minutes_to=minutes_to,
                        )
        db.session.add(timing)
        db.session.commit()
        flash('Вы успешно зарегистрировались')

        return redirect(url_for('doctor.timing'))


class DoctorCasesView(AuthRequiredMethodView):
    def get(self):
        title = 'Записи к врачу'
        cases = None
        if current_user.is_registrator:
            cases = Case.query.all()
        return render_template('doctor/cases.html',
                               title=title,
                               cases=cases)


class DoctorCaseAdd(AuthRequiredMethodView):
    def get(self):
        title = 'Добавить запись'
        cases_add_form = CasesAddForm()
        doctors = Doctor.query.filter(Doctor.role == 'doc')
        return render_template('doctor/cases_add.html',
                               title=title,
                               form=cases_add_form,
                               doctors=doctors)

    def post(self):
        date = datetime.strptime(request.form.get('date'), '%d.%m.%Y')
        diagnosis = request.form.get('diagnosis')
        patient_surename = request.form.get('patient_surename')
        doctor_id = request.form.get('doc')
        new_case = Case(date=date,
                        diagnosis=diagnosis,
                        patient_surename=patient_surename,
                        doctor_id=doctor_id)
        db.session.add(new_case)
        db.session.commit()
        flash('Вы успешно зарегистрировались')

        return redirect(url_for('doctor.cases'))


blueprint.add_url_rule('/', view_func=DoctorIndexView.as_view('index'))
blueprint.add_url_rule('/login', view_func=DoctorLoginView.as_view('login'))
blueprint.add_url_rule('/process_login', view_func=DoctorsLoginProcessView.as_view('process_login'))
blueprint.add_url_rule('/logout', view_func=DoctorLogoutView.as_view('logout'))

blueprint.add_url_rule('/timing', view_func=DoctorTimingView.as_view('timing'))
blueprint.add_url_rule('/timing_add', view_func=DoctorTimingAdd.as_view('timing_add'))
blueprint.add_url_rule('/cases', view_func=DoctorCasesView.as_view('cases'))
blueprint.add_url_rule('/cases_add', view_func=DoctorCaseAdd.as_view('cases_add'))
