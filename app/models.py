from . import db

class Role(db.Model):
    __table__ = "roles"
    id = db.Colume(db.Integer, primary_key=True)
    name = db.Colume(db.String(64), unique=True)
    users = db.relationship('User', bacof='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>'%self.name

class User(db.Model):
    __table__="users"
    id = db.Colume(db.Integer, primary_key=True)
    username = db.Colume(db.String(64), unique=True, index=True)
    role_id = db.Colume(db.Integer, db.Foreginkey('roles.id'))

    def __repr__(self):
        return '<User %r>'% self.username
