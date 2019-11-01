from flask import render_template, current_app
from flask import Blueprint

import webapp.helpers.data_mos_ru_helpers as dms_helper
from webapp.helpers.parsing.get_information import get_data
from webapp.helpers.parsing.get_page import get_html
from webapp.common.views import AuthRequiredMethodView


blueprint = Blueprint('clinic', __name__)


class MoscowClinicsListView(AuthRequiredMethodView):
    def get(self):
        title = 'Список больниц Москвы'
        clinics_list = dms_helper.fetch_clinics_list()
        extract_clinics_list = dms_helper.get_result_clinics_list(clinics_list)
        return render_template('clinic/moscow_clinic_list.html',
                               title=title,
                               clinics_list=extract_clinics_list,
                               )


class NeuroReabClinicsListView(AuthRequiredMethodView):
    def get(self):
        url = current_app.config['NEUROREAB_URL']
        title = f'Список больниц с {url}'
        clinics_list = get_data(get_html(url))
        return render_template('clinic/parse_and_show.html',
                               title=title,
                               clinics_list=clinics_list,
                               )


blueprint.add_url_rule('/moscow_clinic_list', view_func=MoscowClinicsListView.as_view('moscow_clinic_list'))
blueprint.add_url_rule('/parse_and_show', view_func=NeuroReabClinicsListView.as_view('parse_and_show'))
