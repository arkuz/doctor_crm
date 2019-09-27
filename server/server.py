from flask import Flask, render_template

import data_mos_ru_helpers as dms_helper


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


if __name__ == '__main__':
    app.run(debug=True)
