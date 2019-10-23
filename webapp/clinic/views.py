from flask import render_template, current_app
from flask_login import current_user
from flask import Blueprint

import webapp.helpers.data_mos_ru_helpers as dms_helper
import webapp.helpers.parsing.get_information
import webapp.helpers.parsing.get_page


blueprint = Blueprint('clinic', __name__)


@blueprint.route('/moscow_clinic_list')
def moscow_clinic_list():
    if current_user.is_authenticated:
        title = 'Список больниц Москвы'
        clinics_list = dms_helper.fetch_clinics_list()
        extract_clinics_list = dms_helper.get_result_clinics_list(clinics_list)
        return render_template('clinic/moscow_clinic_list.html',
                               title=title,
                               clinics_list=extract_clinics_list,
                               )
    return 'Ошибка, вы не авторизованы!'


@blueprint.route('/parse_and_show')
def parse_and_show():
    if current_user.is_authenticated:
        url = current_app.config['NEUROREAB_URL']
        title = f'Список больниц с {url}'
        clinics_list = webapp.helpers.parsing.get_information.get_data(webapp.helpers.parsing.get_page.get_html(url))
        return render_template('clinic/parse_and_show.html',
                               title=title,
                               clinics_list=clinics_list,
                               )
    return 'Ошибка, вы не авторизованы!'
