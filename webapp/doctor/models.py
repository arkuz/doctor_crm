from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

from webapp.db import db


class Doctor(db.Model, UserMixin):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True) # noqa
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=True)
    specialization = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    role = db.Column(db.String, nullable=True)
    active = db.Column(db.Boolean, nullable=False)

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_registrator(self):
        return self.role == 'registrator'

    @property
    def is_doctor(self):
        return self.role == 'doc'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def json_dump(self):
        return {
            'id': self.id,
            'email': self.email,
            'surname': self.surname,
            'specialization': self.specialization,
            'address': self.address,
            'role': self.role,
        }

    def __repr__(self):
        return '<Doctor {0} {1} {2} {3}>'.format(self.surname, self.email, self.specialization, self.role)


class Timing(db.Model):
    __tablename__ = 'timing'
    id = db.Column(db.Integer, primary_key=True) # noqa
    doctor_id = db.Column(db.Integer,
                          db.ForeignKey('doctor.id', ondelete='CASCADE'),
                          index=True)
    day = db.Column(db.DateTime, nullable=True, default=datetime.date.today())
    hours_with = db.Column(db.Integer, nullable=True, default=9)
    minutes_with = db.Column(db.Integer, nullable=True, default=0)
    hours_to = db.Column(db.Integer, nullable=True, default=18)
    minutes_to = db.Column(db.Integer, nullable=True, default=0)
    doctor = db.relationship('Doctor', backref='timing')

    def __repr__(self):
        return '<Timing {0} {1}>'.format(self.doctor_id, self.day)
