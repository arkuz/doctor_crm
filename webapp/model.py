from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Doctor(db.Model):
    __tablename__ = 'doctor'
    doctor_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=True)
    specialization = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=True)
    case = db.relationship('Case', backref='doctor')

    def json_dump(self):
        return {
            'doctor_id': self.doctor_id,
            'email': self.email,
            'surname': self.surname,
            'specialization': self.specialization,
            'address': self.address,
            'is_admin': self.is_admin,
        }

    def __repr__(self):
        return '<Doctor {0} {1} {2} {3}>'.format(self.surname, self.email, self.specialization, self.is_admin)


class Patient(db.Model):
    __tablename__ = 'patient'
    patient_id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String, nullable=True)
    birthdate = db.Column(db.DateTime, nullable=True)
    city = db.Column(db.String, nullable=True)
    sex = db.Column(db.Boolean, nullable=True)
    case = db.relationship('Case', backref='patient')

    def json_dump(self):
        return {
            'patient_id': self.patient_id,
            'surname': self.surname,
            'birthdate': self.birthdate,
            'city': self.city,
            'sex': self.sex,
        }

    def __repr__(self):
        return '<Patient {0}>'.format(self.surname)


class Case(db.Model):
    __tablename__ = 'case'
    case_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=True)
    diagnosis = db.Column(db.String, nullable=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))

    def json_dump(self):
        return {
            'case_id': self.case_id,
            'date': self.date,
            'diagnosis': self.diagnosis,
            'doctor_id': self.doctor_id,
            'patient_id': self.patient_id,
        }

    def __repr__(self):
        return '<Case {0} {1} {2} {3}>'.format(self.doctor_id, self.patient_id, self.diagnosis, self.date)
