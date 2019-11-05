import sys

from webapp import create_app
from webapp.db import db
from webapp.doctor.models import Timing


app = create_app()

timing = [
    {
        'doctor_id': 1,
        'hours_with': 8,
        'minutes_with': 30,
        'hours_to': 18,
        'minutes_to': 0,
    },
    {
        'doctor_id': 2,
        'hours_with': 8,
        'minutes_with': 30,
        'hours_to': 18,
        'minutes_to': 0,
    },
    {
        'doctor_id': 3,
        'hours_with': 8,
        'minutes_with': 30,
        'hours_to': 18,
        'minutes_to': 0,
    },
    {
        'doctor_id': 3,
        'hours_with': 8,
        'minutes_with': 30,
        'hours_to': 18,
        'minutes_to': 0,
    },
    {
        'doctor_id': 4,
        'hours_with': 8,
        'minutes_with': 30,
        'hours_to': 18,
        'minutes_to': 0,
    },
]

with app.app_context():

    for item in timing:
        new_Timing = Timing(
            doctor_id=item['doctor_id'],
            hours_with=item['hours_with'],
            minutes_with=item['minutes_with'],
            hours_to=item['hours_to'],
            minutes_to=item['minutes_to'],
        )
        db.session.add(new_Timing)
        db.session.commit()
        print('Timing with id {} added'.format(new_Timing.id)) # noqa

print('Test Timings added') # noqa
sys.exit(0)
