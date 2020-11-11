from flask import render_template, request, redirect, url_for
from app import app
from app.models import Locations, Birds, Sightings
from app import db
from app.locationform import locationForm
from app.birdform import birdForm
from app.form import sightingForm

@app.route('/')
def index():
        all_locations = Locations.query.all()
        all_birds = Birds.query.all()
        all_sightings = Sightings.query.all()
        return render_template('index.html', all_locations=all_locations, all_birds=all_birds, all_sightings=all_sightings)

@app.route('/add/location', methods=['GET', 'POST'])
def addlocation():
    form = locationForm()
    location = Locations(place_name = form.place_name.data, county = form.county.data, country = form.country.data)
    db.session.add(location)
    db.session.commit()
    return redirect (url_for('index'))
    return render_template('locationform.html', form=form)

@app.route('/add/bird', methods=['GET', 'POST'])
def addbird():
    form = birdForm()
    bird = Birds(scientific_name = form.scientific_name.data, common_name = form.common_name.data)
    db.session.add(bird)
    db.session.commit()
    return redirect (url_for('index'))
    return render_template('birdform.html', form=form)

@app.route('/add/sighting', methods=['GET', 'POST'])
def addsighting():
    form = sightingForm()
    sighting = Sightings(location_id = form.location_id.data, bird_id = form.bird_id.data, recorded = form.recorded.data, gender = form.gender.data, life_stage = form.life_stage.data, number = form.number.data)
    db.session.add(sighting)
    db.session.commit()
    return redirect (url_for('index'))
    return render_template('form.html', form=form)

@app.route('/update/location', methods=['GET', 'POST'])
def updatelocation(id):
        form = locationForm()
        location_to_update = Locations.query.get(id)
        db.session.commit()
        if request.method == 'GET':
                form.place_name.data = location_to_update.place_name
                form.county.data = location_to_update.county
                form.country.data = location_to_update.country
        return redirect(url_for('index'))
        return render_template('locationupdate.html', form=form)

@app.route('/update/bird', methods=['GET', 'POST'])
def updatebird(id):
        form = birdForm()
        bird_to_update = Birds.query.get(id)
        db.session.commit()
        if request.method == 'GET':
                form.scientific_name.data = bird_to_update.scientific_name
                form.common_name.data = bird_to_update.scientific_name
        return redirect(url_for('index'))
        return render_template('birdupdate.html', form=form)

@app.route('/update/sighting', methods=['GET', 'POST'])
def updatesighting(id):
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

@app.route('/delete/location', methods=['POST'])
def deletelocation(id):
        location = Locations.query.get(id)
        db.session.delete(location)
        db.session.commit()
        return redirect(url_for('index')

@app.route('/delete/bird', methods=['POST'])
def deletebird(id):
        bird = Birds.query.get(id)
        db.session.delete(bird)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/delete/sighting', methods=['POST'])
def deletesighting(id):
        sighting = Sightings.query.get(id)
        db.session.delete(sighting)
        db.session.commit()
        return redirect(url_for('index'))
