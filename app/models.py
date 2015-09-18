from datetime import datetime

# import the db from main
from app import db


# Models goes here....
class _module1(db.Model):
    __tablename__ = '_module1'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_name = db.Column(db.String(20), nullable= False, unique=True, index=True)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
