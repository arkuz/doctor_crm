import os
import requests


def fetch_clinics_list() -> list:
    """ Функция для получения списка больниц от сервиса https://apidata.mos.ru. """
    url = 'https://apidata.mos.ru/v1/datasets/517/rows'
    params = {
        'api_key': os.environ['DATA_MOS_RU_API_KEY'],
    }
    try:
        resp = requests.get(url, params=params)
    except (requests.RequestException, ValueError):
        return None
    if resp:
        resp = resp.json()
        for line in resp:
            yield line


def extract_clinics_data(clinic_data) -> dict:
    """ Функция для выборки нужных данных из ответа get_clinics_list()."""
    try:
        return {
            'name': clinic_data['Cells']['FullName'],
            'address': clinic_data['Cells']['OrgInfo'][0]['LegalAddress'],
            'latitude': clinic_data['Cells']['geoData']['coordinates'][0][0],
            'longitude': clinic_data['Cells']['geoData']['coordinates'][0][1],
        }
    except KeyError:
        pass


def get_result_clinics_list(clinics_generator) -> list:
    """ Функция для создания итогового списка клиник. """
    extract_clinics_list = []
    if clinics_generator is not None:
        for clinic in clinics_generator:
            extract_clinics_list.append(extract_clinics_data(clinic))
    return extract_clinics_list
