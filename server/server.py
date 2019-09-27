from flask import Flask, render_template

import data_mos_ru_helpers as dms_helper
import parsing.get_information
import parsing.get_page


app = Flask(__name__)


@app.route('/')
def index():
    title = 'Список больниц Москвы'
    clinics_list = dms_helper.fetch_clinics_list()
    extract_clinics_list = dms_helper.get_result_clinics_list(clinics_list)
    return render_template('index.html',
                           title=title,
                           clinics_list=extract_clinics_list,
                           )


@app.route('/parse_and_show')
def parse_and_show():
    title = 'Список больниц с http://neuroreab.ru/centers/'
    url = 'http://neuroreab.ru/centers/'
    clinics_list = parsing.get_information.get_data(parsing.get_page.get_html(url))
    return render_template('parse_and_show.html',
                           title=title,
                           clinics_list=clinics_list,
                           )


if __name__ == '__main__':
    app.run(debug=True)
