from flask import render_template, request, redirect, url_for
from app import app
from app.models import Locations, Birds, Sightings
from app import db
from app.form import locationForm, birdForm, sightingForm

@app.route('/')
def index():
        all_locations = Locations.query.all()
        all_birds = Birds.query.all()
        all_sightings = Sightings.query.all()
        return render_template('index.html', all_locations=all_locations, all_birds=all_birds, all_sightings=all_sightings)

@app.route('/add/location', methods=['GET', 'POST'])
def addlocation():
    form = locationForm()
    if form.validate_on_submit():
        location = Locations(place_name = form.place_name.data, county = form.county.data, country = form.country.data)
        db.session.add(location)
        db.session.commit()
        return redirect (url_for('index'))
    return render_template('locationform.html', form=form)

@app.route('/add/bird', methods=['GET', 'POST'])
def addbird():
    form = birdForm()
    if form.validate_on_submit():
        bird = Birds(scientific_name = form.scientific_name.data, common_name = form.common_name.data)
        db.session.add(bird)
        db.session.commit()
        return redirect (url_for('index'))
    return render_template('birdform.html', form=form)

@app.route('/add/sighting', methods=['GET', 'POST'])
def addsighting():
    form = sightingForm()
    if form.validate_on_submit():
        sighting = Sightings(location_id = form.location_id.data, bird_id = form.bird_id.data, recorded = form.recorded.data, gender = form.gender.data, life_stage = form.life_stage.data, number = form.number.data)
        db.session.add(sighting)
        db.session.commit()
        return redirect (url_for('index'))
    return render_template('form.html', form=form)

@app.route('/update/location/<int:id>', methods=['GET', 'POST'])
def updatelocation(id):
        form = locationForm()
        location = Locations.query.get(id)
        if form.validate_on_submit:
            location.place_name = form.place_name.data
            location.county = form.county.data
            location.country = form.country.data
            db.session.commit()
            return redirect(url_for('index'))
        elif request.method == 'GET':
            form.place_name.data = location.place_name
            form.county.data = location.county
            form.country.data = location.country
        return render_template('locationupdate.html', form=form)

@app.route('/update/bird/<int:id>', methods=['GET', 'POST'])
def updatebird(id):
        form = birdForm()
        bird = Birds.query.get(id)
        if form.validate_on_submit():
            bird.scientific_name = form.scientific_name.data
            bird.common_name = form.common_name.data
            db.session.commit()
            return redirect(url_for('index'))
        elif request.method == 'GET':
            form.scientific_name.data = bird.scientific_name
            form.common_name.data = bird.common_name
        return render_template('birdupdate.html', form=form)

@app.route('/update/sighting/<int:id>', methods=['GET', 'POST'])
def updatesighting(id):
        form = sightingForm()
        sighting = Sightings.query.get(id)
        if form.validate_on_submit():
            sighting.location_id = form.location_id.data
            sighting.bird_id = form.bird_id.data
            sighting.recorded = form.recorded.data
            sighting.gender = form.gender.data
            sighting.life_stage = form.life_stage.data
            sighting.number = form.number.data
            db.session.commit()
            return redirect(url_for('index'))
        elif request.method == 'GET':
            form.location_id.data = sighting.location_id
            form.bird_id.data = sighting.bird_id
            form.recorded.data = sighting.recorded
            form.gender.data = sighting.gender
            form.life_stage.data = sighting.life_stage
            form.number.data = sighting.number
        return render_template('update.html', form=form)

@app.route('/delete/location/<int:id>', methods=['GET'])
def deletelocation(id):
        location = Locations.query.get(id)
        db.session.delete(location)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/delete/bird/<int:id>', methods=['GET'])
def deletebird(id):
        bird = Birds.query.get(id)
        db.session.delete(bird)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/delete/sighting/<int:id>', methods=['GET'])
def deletesighting(id):
        sighting = Sightings.query.get(id)
        db.session.delete(sighting)
        db.session.commit()
        return redirect(url_for('index'))
