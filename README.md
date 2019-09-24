[![Build Status](https://travis-ci.org/arkuz/doctor_crm.svg?branch=master)](https://travis-ci.org/arkuz/doctor_crm)
#### Описание
Медицинская CRM система "Doctor CRM"
 
 
#### Требования к ПО
- Установленный Python 3.7
- Установленный инструмент для работы с виртуальными окружениями virtualenv
```bash
pip install virtualenv
```

#### Установка
```bash
git clone https://github.com/arkuz/doctor_crm
cd tm_bot
virtualenv env
env/scripts/activate
pip install -r requirements.txt
```

#### Запуск

Перед запуском необходимо заполнить переменные окружения с настройками.

- `DATA_MOS_RU_API_KEY` - ключ API сервиса https://apidata.mos.ru
```bash
set DATA_MOS_RU_API_KEY=aaaaaaaaaaaaaaaaaaaaaaaa
python server.py
```
 - Открыть в браузере адрес http://127.0.0.1:5000/