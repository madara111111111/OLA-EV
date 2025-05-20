from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'admin' or 'viewer'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(300))
    text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(10))  # 'positive', 'neutral', 'negative'

class Showroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    location = db.Column(db.String(300))
    google_maps_link = db.Column(db.String(500))

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(200))
    price = db.Column(db.String(50))
    features = db.Column(db.Text)
