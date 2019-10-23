from flask import render_template
from flask_login import current_user, login_required

import webapp.helpers.data_mos_ru_helpers as dms_helper
import webapp.parsing.get_information
import webapp.parsing.get_page






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
