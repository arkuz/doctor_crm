from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Users {0} {1}>'.format(self.title, self.url)
