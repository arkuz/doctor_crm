from flask import render_template, current_app
from flask_login import current_user
from flask import Blueprint
from flask.views import MethodView

import webapp.helpers.data_mos_ru_helpers as dms_helper
from webapp.helpers.parsing.get_information import get_data
from webapp.helpers.parsing.get_page import get_html


blueprint = Blueprint('clinic', __name__)


class MoscowClinicsListView(MethodView):
    def get(self):
        if current_user.is_authenticated:
            title = 'Список больниц Москвы'
            clinics_list = dms_helper.fetch_clinics_list()
            extract_clinics_list = dms_helper.get_result_clinics_list(clinics_list)
            return render_template('clinic/moscow_clinic_list.html',
                                   title=title,
                                   clinics_list=extract_clinics_list,
                                   )
        return 'Ошибка, вы не авторизованы!'


class NeuroReabClinicsListView(MethodView):
    def get(self):
        if current_user.is_authenticated:
            url = current_app.config['NEUROREAB_URL']
            title = f'Список больниц с {url}'
            clinics_list = get_data(get_html(url))
            return render_template('clinic/parse_and_show.html',
                                   title=title,
                                   clinics_list=clinics_list,
                                   )
        return 'Ошибка, вы не авторизованы!'


blueprint.add_url_rule('/moscow_clinic_list', view_func=MoscowClinicsListView.as_view('moscow_clinic_list'))
blueprint.add_url_rule('/parse_and_show', view_func=NeuroReabClinicsListView.as_view('parse_and_show'))
