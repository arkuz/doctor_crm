from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.model import db

class Doctor(db.Model, UserMixin):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True) # noqa
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=True)
    specialization = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=True)

    @property
    def is_administrator(self):
        return self.is_admin

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
            'is_admin': self.is_admin,
        }

    def __repr__(self):
        return '<Doctor {0} {1} {2} {3}>'.format(self.surname, self.email, self.specialization, self.is_admin)