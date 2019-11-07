from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
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


class TimingAddForm(FlaskForm):
    day = DateField('Дата',
                    validators=[DataRequired()],
                    render_kw={
                        'class': 'form-control',
                        'autofocus': True,
                        'placeholder': 'mm.dd.yyyy',
                    })

    hours_with = IntegerField('Часы с',
                              validators=[DataRequired()],
                              render_kw={
                                  'class': 'form-control',
                              })

    minutes_with = IntegerField('Минуты с',
                                validators=[DataRequired()],
                                render_kw={
                                    'class': 'form-control',
                                })

    hours_to = IntegerField('Часы по',
                            validators=[DataRequired()],
                            render_kw={
                                'class': 'form-control',
                            })

    minutes_to = IntegerField('Минуты по',
                              validators=[DataRequired()],
                              render_kw={
                                  'class': 'form-control',
                              })

    add = SubmitField('Добавить',
                      render_kw={
                          'class': 'btn btn-primary',
                      })


class CasesAddForm(FlaskForm):
    patient_surename = StringField(
        'Пациент',
        validators=[DataRequired()],
        render_kw={
            'class': 'form-control',
            'autofocus': True,
        })
    date = DateField(
        'Дата',
        validators=[DataRequired()],
        render_kw={
            'class': 'form-control',
            'placeholder': 'mm.dd.yyyy',
        })

    diagnosis = StringField('Диагноз',
                            validators=[DataRequired()],
                            render_kw={
                                'class': 'form-control',
                            })

    add = SubmitField('Добавить',
                      render_kw={
                          'class': 'btn btn-primary',
                      })
