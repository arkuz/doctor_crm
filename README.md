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
cd doctor_crm
virtualenv env
env/scripts/activate
pip install -r requirements.txt
```

#### Запуск

Перед запуском необходимо заполнить файл с настройками `config.py`, а так же выполнить скрипт создания БД `create_db.py`
```bash
python create_db.py
```

Запускаем приложение:
```bash
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```
Открыть в браузере адрес http://127.0.0.1:5000/
