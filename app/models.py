from datetime import datetime

# import the db from main
from . import db


# Models goes here....
class _module1(db.Model):
    __tablename__ = '_module1'
    id = db.Column(db.intger, primary_key=True)
    created_at = db.Column(db.Datetime(), default=datetime.utcnow)
