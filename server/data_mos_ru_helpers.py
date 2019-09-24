import os
import requests


def get_clinics_list() -> list:
    """ Функция для получения списка больниц от сервиса https://apidata.mos.ru. """
    url = 'https://apidata.mos.ru/v1/datasets/517/rows'
    params = {
        'api_key': os.environ['DATA_MOS_RU_API_KEY'],
    }
    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return resp.json()
    except (requests.RequestException, ValueError):
        return None


def extract_clinics_data(clinics_list) -> list:
    """ Функция для выборки нужных данных из ответа get_clinics_list()."""
    clinics_list_result = []
    try:
        for clinic in clinics_list:
            clinics_list_result.append({
                'name': clinic['Cells']['FullName'],
                'address': clinic['Cells']['OrgInfo'][0]['LegalAddress'],
                'latitude': clinic['Cells']['geoData']['coordinates'][0][0],
                'longitude': clinic['Cells']['geoData']['coordinates'][0][1],
            })
    except KeyError:
        pass
    return clinics_list_result
