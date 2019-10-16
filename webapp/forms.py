from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Электронная почта',
                        validators=[DataRequired()],
                        render_kw={
                            'class': 'form-control',
                            'autofocus': True,
                        })

    password = PasswordField('Пароль',
                             validators=[DataRequired()],
                             render_kw={
                                 'class': 'form-control',
                             })

    login = SubmitField('Войти',
                        render_kw={
                            'class': 'btn btn-primary',
                        })

    reg = SubmitField('Зарегистрироваться',
                      render_kw={
                          'class': 'btn btn-link',
                      })
