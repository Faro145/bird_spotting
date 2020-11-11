from flask import render_template, request, redirect, url_for
from app import app
from app.models import Locations, Birds, Sightings
from app import db
from app.form import sightingForm

@app.route('/')
def index():
        all_sightings = Sightings.query.all()
        return render_template('index.html', all_sightings=all_sightings)

@app.route('/add/sighting', methods=['GET', 'POST'])
def addsighting():
    form = sightingForm()
    sighting = Sightings(location_id = form.location_id.data, bird_id = form.bird_id.data, recorded = form.recorded.data, gender = form.gender.data, life_stage = form.life_stage.data, number = form.number.data)
    db.session.add(sighting)
    db.session.commit()
    return redirect (url_for('index'))
    return render_template('form.html', form=form)

@app.route('/update', methods=['GET', 'POST'])
def update(id):
        form = sightingForm()
        sighting_to_update = Sightings.query.get(id)
        db.session.commit()
        if request.method == 'GET':
                form.location_id.data = sighting_to_update.location_id
                form.bird_id.data = sighting_to_update.bird_id
                form.recorded.data = sighting_to_update.recorded
                form.gender.data = sighting_to_update.gender
                form.life_stage.data = sighting_to_update.life_stage
                form.number.data = sighting_to_update.number
        return redirect(url_for('index'))
        return render_template('update.html', form=form)

@app.route('/delete', methods=['POST'])
def delete(id):
        sighting = Sightings.query.get(id)
        db.session.delete(sighting)
        db.session.commit()
        return redirect(url_for('index'))
