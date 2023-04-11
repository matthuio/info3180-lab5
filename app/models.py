from flask import Flask
from app import db
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# Add any model classes for Flask-SQLAlchemy here

class movie(db.model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text(80))
    poster = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.now())

def __init__(self, title, description, poster):
    self.title = title
    self.description = description
    self.poster = poster
    self.created_at = datetime.now()
