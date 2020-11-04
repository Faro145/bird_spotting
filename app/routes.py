from flask import render_template, request, redirect, url_for
from app import app
from app.models import Locations, Birds, Sightings
from app import db

@app.route('/')
def index():
        sightings = Sightings.query.all()
        return render_template('index.html'), sightings=sightings)

@app.route('/add', methods=['POST'])
def add():
        sighting = Sightings(text=request.form('sighting'))
        db.session.add(sighting)
        db.session.commit()
        return redirect (url_for('index'))

@app.route('/update', methods=['POST'])
def update():
        sighting_to_update = Sightings.query.get(id)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
        sighting = Sightings.query.get(id)
        db.session.delete(sighting)
        db.session.commit()
        return redirect(url_for('index'))
