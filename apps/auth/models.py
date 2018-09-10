from .. import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return '<User {0} id: {1}>'.format(self.username, self.id)

    def __str__(self):
        return self.__repr__()

    def is_active(self):
        return self.active

    def is_authenticated(self):
        pass
