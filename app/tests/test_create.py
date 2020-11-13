import unittest
from flask import url_for
from flask_testing import TestCase
from app import app, db
from app.models import Locations, Birds, Sightings

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        db.create_all()
        location = Locations(id = 1, place_name = "Bennachie", county = "Aberdeenshire", country = "Scotland")
        bird = Birds(id = 1, scientific_name = "Motacilla alba", common_name "Pied Wagtail")
        sighting = Sightings(location_id = 1, bird_id = 1, recorded = 24/06/2015, gender = "Male", life_stage = "Adult", number = 2)
        db.session.add(location)
        db.session.add(bird)
        db.session.add(sighting)
        db.session.commit()

