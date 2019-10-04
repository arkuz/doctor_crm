import os
basedir = os.path.abspath(os.path.dirname('__file__'))

# путь к БД
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'webapp.db')

# ключ API сервиса https://apidata.mos.ru
DATA_MOS_RU_API_KEY = ''

# соль для паролей пользователей
PASSWORD_SALT = ''

# секретный ключ для сессии
SESSION_SECRET_KEY = b''
