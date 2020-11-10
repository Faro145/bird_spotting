from app import db

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String(100), nullable = False)
    county = db.Column((db.String(30)), nullable = False)
    country = db.Column((db.String(30)), nullable = False)
    sightings = db.relationship('Sightings', backref='locations')

class Birds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scientific_name = db.Column(db.String(100), nullable = False)
    common_name = db.Column((db.String(30)), nullable = False)
    sightings = db.relationship('Sightings', backref='animals')

class Sightings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column('locations_id', db.Integer, db.ForeignKey('locations.id'))
    bird_id = db.Column('birds_id', db.Integer, db.ForeignKey('birds.id'))
    recorded = db.Column('Date', db.String(30), nullable = False)
    gender = db.Column((db.String(10)), nullable = False)
    life_stage = db.Column((db.String(20)), nullable = False)
    number = db.Column(db.Integer, nullable = False)
