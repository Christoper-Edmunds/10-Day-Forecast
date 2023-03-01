from sqlalchemy import func
from . import db 

class weatherdatabase(db.Model):
    id = db.Column('Id', db.Integer, primary_key=True)
    latitude = db.Column('Latitude', db.Float)
    longitude = db.Column('Longitude', db.Float)
