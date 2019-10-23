from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Case(db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True) # noqa
    date = db.Column(db.DateTime, nullable=True)
    diagnosis = db.Column(db.String, nullable=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    doctor = db.relationship('Doctor')
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
