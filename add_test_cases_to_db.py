import sys

from webapp import create_app
from webapp.db import db
from webapp.case.models import Case


app = create_app()

cases = [
    {
        'diagnosis': 'Болезни органов дыхания',
        'doctor_id': 3,
        'patient_id': 1,
        'patient_surename': 'Иванов',
    },
    {
        'diagnosis': 'Болезни органов пищеварения',
        'doctor_id': 3,
        'patient_id': 2,
        'patient_surename': 'Петров',
    },
    {
        'diagnosis': 'Инфекционные заболевания',
        'doctor_id': 3,
        'patient_id': 1,
        'patient_surename': 'Пупкин',
    },
    {
        'diagnosis': 'Болзени сердечно-сосудистой системы',
        'doctor_id': 3,
        'patient_id': 2,
        'patient_surename': 'Семенов',
    },
    {
        'diagnosis': 'Новообразования',
        'doctor_id': 3,
        'patient_id': 1,
        'patient_surename': 'Антонов',
    },

]

with app.app_context():

    for item in cases:
        new_cases = Case(
            diagnosis=item['diagnosis'],
            doctor_id=item['doctor_id'],
            patient_id=item['patient_id'],
            patient_surename=item['patient_surename'],
        )
        db.session.add(new_cases)
        db.session.commit()
        print('Cases with id {} added'.format(new_cases.id)) # noqa

print('Test Cases added') # noqa
sys.exit(0)
