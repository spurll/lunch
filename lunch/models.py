from __future__ import division
from lunch import app, db


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    votes = db.relationship('Vote', backref='user', lazy='dynamic')
    favourites = db.relationship('Favourite', backref='user', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_admin(self):
        return self.id in app.config["ADMIN_USERS"]

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Vote(db.Model):
    type = db.Column(db.String(128), primary_key=True)
    option = db.Column(db.String(128), primary_key=True)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __repr__(self):
        return '<Vote {}: {}>'.format(self.option, self.score)


class Favourite(db.Model):
    type = db.Column(db.String(128), primary_key=True)
    option = db.Column(db.String(128), primary_key=True)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __repr__(self):
        return '<Favourite {}: {}>'.format(self.option, self.score)


class History(db.Model):
    type = db.Column(db.String(128), primary_key=True)
    option = db.Column(db.String(128), primary_key=True)
    total = db.Column(db.Integer)
    ballots = db.Column(db.Integer)

    def __repr__(self):
        return '<History {}: {}>'.format(self.option, self.score())

    def score(self):
        return self.total / self.ballots    # Floating-point division, future.

