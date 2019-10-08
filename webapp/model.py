from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Users {0} {1}>'.format(self.title, self.url)


class MedicalSpecialist(db.Model):
    __tablename__ = 'specialist'
    specialist_id = db.Column(db.Integer, primary_key=True)
    specialist_surename = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    hospital = db.Column(db.String, nullable=True)
    department = db.Column(db.String, nullable=True)
    patient = db.relationship(
        'Patient', backref='specialist')


class Patient(db.Model):
    __tablename__ = 'patient'
    patient_id = db.Column(db.Integer, primary_key=True)
    patient_surename = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    disease = db.Column(db.String, nullable=True)
    specialist_id = db.Column(
        db.Integer, db.ForeignKey('specialist.specialist_id'))
