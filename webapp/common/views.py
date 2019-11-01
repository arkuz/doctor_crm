from flask_login import current_user
from flask import Blueprint
from flask.views import MethodView


blueprint = Blueprint('common', __name__)


class AuthRequiredMethodView(MethodView):
    def dispatch_request(self, *args, **kwargs):
        if not current_user.is_authenticated:
            return 'Ошибка, вы не авторизованы!'
        else:
            return super().dispatch_request(*args, **kwargs)
