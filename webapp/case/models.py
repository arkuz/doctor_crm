from webapp.db import db
import datetime


class Case(db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True) # noqa
    date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now())
    diagnosis = db.Column(db.String, nullable=True)
    patient_surename = db.Column(db.String, nullable=True)
    doctor_id = db.Column(db.Integer,
                          db.ForeignKey('doctor.id', ondelete='CASCADE'),
                          index=True,
                          nullable=True,
                          )
    patient_id = db.Column(db.Integer,
                           db.ForeignKey('patient.id', ondelete='CASCADE'),
                           index=True,
                           nullable=True,
                           )
    doctor = db.relationship('Doctor', backref='case')
    patient = db.relationship('Patient', backref='case')

    def json_dump(self):
        return {
            'id': self.id, # noqa
            'date': self.date,
            'diagnosis': self.diagnosis,
            'patient_surename': self.patient_surename,
        }

    def __repr__(self):
        return '<Case {0} {1} {2} {3}>'.format(self.id, self.patient_surename, self.diagnosis, self.date)
