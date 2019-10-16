from webapp.model import db, Doctor


def is_user_exist(email):
    return Doctor.query.filter(Doctor.email == email).count()


def registration(email, password):
    reg_success = False
    if not is_user_exist(email):
        doctor = Doctor(email=email)
        doctor.set_password(password)
        db.session.add(doctor)
        db.session.commit()
        reg_success = True
    return reg_success
