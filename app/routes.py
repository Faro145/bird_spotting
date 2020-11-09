from flask import render_template, request, redirect, url_for
from app import app
from app.models import Locations, Birds, Sightings
from app import db
from app.forms import sightingForm

@app.route('/')
def index():
        all_sightings = Sightings.query.all()
        return render_template('index.html'), all_sightings=all_sightings)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = sightingform()
    sighting = Sightings(location_id = form.location_id.data, bird_id = form.bird_data, recorded = form.recorded.data, gender = form.gender.data, life_stage = form.life_stage.data, number = form.number.data)
    db.session.add(sighting)
    db.session.commit()
    return redirect (url_for('index'))
    return render_template('form.html', form=form)

@app.route('/update', methods=['POST'])
def update(id):
        sighting_to_update = Sightings.query.get(id)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete(id):
        sighting = Sightings.query.get(id)
        db.session.delete(sighting)
        db.session.commit()
        return redirect(url_for('index'))