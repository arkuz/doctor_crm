from webapp.db import db


class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True) # noqa
    surname = db.Column(db.String, nullable=True)
    birthdate = db.Column(db.DateTime, nullable=True)
    city = db.Column(db.String, nullable=True)
    sex = db.Column(db.Boolean, nullable=True)

    def json_dump(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'birthdate': self.birthdate,
            'city': self.city,
            'sex': self.sex,
        }

    def __repr__(self):
        return '<Patient {0}>'.format(self.surname)
