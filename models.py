from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150), nullable=False)
    lname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone = db.Column(db.String(150), nullable=False, unique=True)
    profile_pic = db.Column(db.String(150), default='default.jpg')
    address = db.Column(db.String(250))
    password = db.Column(db.String(150), nullable=False)


