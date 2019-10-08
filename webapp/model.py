from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'doctor'
    doctor_id = db.Column(db.Integer, primary_key=True)
    doctor_email = db.Column(db.String, nullable=True)
    doctor_password = db.Column(db.String, nullable=True)
    doctor_surename = db.Column(db.String, nullable=True)
    doctor_specialization = db.Column(db.String, nullable=True)
    doctor_city = db.Column(db.String, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=True)
    case = db.relationship('case', backref='doctor')

    def __repr__(self):
        return '<Users {0} {1}>'.format(self.title, self.url)


class Patient(db.Model):
    __tablename__ = 'patient'
    patient_id = db.Column(db.Integer, primary_key=True)
    patient_surename = db.Column(db.String, nullable=True)
    patient_birthdate = db.Column(db.DateTime, nullable=True)
    patient_city = db.Column(db.String, nullable=True)
    patient_sex = db.Column(db.Boolean, nullable=True)
    case = db.relationship('case', backref='patient')

    def __repr__(self):
        return '<Patients {0} {1}>'.format(self.title, self.url)


class Case(db.Model):
    __tablename__ = 'case'
    case_id = db.Column(db.Integer, primary_key=True)
    case_date = db.Column(db.DateTime, nullable=True)
    case_diagnosis = db.Column(db.String, nullable=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))

    def __repr__(self):
        return '<Cases {0} {1}>'.format(self.title, self.url)
