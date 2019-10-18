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

- Перед запуском необходимо заполнить файл с настройками `config.py`.
- Выполнить скрипт создания БД `create_db.py`
```bash
python create_db.py
```

- Выполнить скрипт генерации тестовых пользователей `add_test_doctors_to_db.py`. 
  - Пользователи: `admin@doc.ru`, `doc1@doc.ru`, `doc2@doc.ru`, `doc3@doc.ru`.
  - Пароль: `123`
```bash
python add_test_doctors_to_db.py
```

 - Если тестовые пользователи не используются, то выполнить скрипт для генерации аккаунта администратора `create_admin.py`.
 ```bash
python create_admin.py
```

- Запускаем приложение:
```bash
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```
Открыть в браузере адрес http://127.0.0.1:5000/
