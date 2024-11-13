# app/models.py

from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    # fields
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    # relationships
    rsvp = db.relationship('RSVP', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # relationships
    rsvps = db.relationship('RSVP', backref='venue', lazy=True)
    
    def __repr__(self):
        return f'<Venue {self.name}>'

class RSVP(db.Model):
    __tablename__ = 'rsvps'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # "Attending" or "Tentative"
    
    def __repr__(self):
        return f'<RSVP {self.user_id}, {self.venue_id}, {self.status}>'