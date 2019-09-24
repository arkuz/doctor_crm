import os
from flask import Flask, render_template

import data_mos_ru_helpers as dms_helper


# ключ API сервиса https://apidata.mos.ru
os.environ['DATA_MOS_RU_API_KEY'] = '40efbeeb79728efe0bc580f6174da03d'

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Список больниц Москвы'
    clinics_list = dms_helper.get_clinics_list()
    if clinics_list:
        clinics_list = dms_helper.extract_clinics_data(clinics_list)
    return render_template('index.html',
                           title=title,
                           clinics_list=clinics_list,
                           )


if __name__ == '__main__':
    app.run(debug=True)
