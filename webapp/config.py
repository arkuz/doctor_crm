import os
basedir = os.path.abspath(os.path.dirname('__file__'))

# путь к БД
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'webapp.db')

# ключ API сервиса https://apidata.mos.ru
DATA_MOS_RU_API_KEY = ''

# соль для паролей пользователей
PASSWORD_SALT = ''

# ключ API для сервиса email рассылок https://sendgrid.com
SENDGRID_API_KEY = ''

# email от лица которого будут отправляться письма пользователям
FROM_EMAIL = ''

# секретный ключ для сессии
SESSION_SECRET_KEY = b''
