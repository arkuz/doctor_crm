import os
basedir = os.path.abspath(os.path.dirname('__file__'))

# путь к БД
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'webapp.db')

# ключ API сервиса https://apidata.mos.ru
DATA_MOS_RU_API_KEY = '40efbeeb79728efe0bc580f6174da03d'

# соль для паролей пользователей
PASSWORD_SALT = 'c8b4df885065976921d20716e4a1a36bb580d0e47076cfab9d421d51f32ee3dc'

# ключ API для сервиса email рассылок https://sendgrid.com
SENDGRID_API_KEY = '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'

# email от лица которого будут отправляться письма пользователям
FROM_EMAIL = 'doctorcrmtest@gmail.com'

# секретный ключ для сессии
SESSION_SECRET_KEY = b'()*&%&087gho9h)'

# сайт для парсинга клиник
NEUROREAB_URL = 'http://neuroreab.ru/centers/'
