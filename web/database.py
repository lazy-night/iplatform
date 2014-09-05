# -*- encoding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from web import app

db = SQLAlchemy(app)
db_session = db.session


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    def __init__(self, name, password):
        self.name = name
        self.password = password


def init_db():
    db.create_all()


def insert_user(name, password):
    user = User.query.filter_by(name=name).first()

    if not user:
        u = User(name, password)
        db.session.add(u)
        db.session.commit()

    return user


def varify_user(name, password):
    user = User.query.filter_by(name=name).first()
    if user:
        if user.password == password:
            return user
        else:
            return None
    else:
        return None
