from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True) # noqa
    surname = db.Column(db.String, nullable=True)
    birthdate = db.Column(db.DateTime, nullable=True)
    city = db.Column(db.String, nullable=True)
    sex = db.Column(db.Boolean, nullable=True)
    # case = db.relationship('Case', backref='patient')

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


class Case(db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True) # noqa
    date = db.Column(db.DateTime, nullable=True)
    diagnosis = db.Column(db.String, nullable=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    #doctor = db.relationship('Doctor')
    patient = db.relationship('Patient')

    def json_dump(self):
        return {
            'id': self.id, # noqa
            'date': self.date,
            'diagnosis': self.diagnosis,
            'id': self.id, # noqa
            'id': self.id, # noqa
        }

    def __repr__(self):
        return '<Case {0} {1} {2} {3}>'.format(self.id, self.id, self.diagnosis, self.date)
