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
        bird = Birds(id = 1, scientific_name = "Motacilla alba", common_name = "Pied Wagtail")
        sighting = Sightings(location_id = 1, bird_id = 1, recorded = "24/06/15", gender = "Male", life_stage = "Adult", number = 2)
        db.session.add(location)
        db.session.add(bird)
        db.session.add(sighting)
        db.session.commit()
    
    def tearDown(self):
         db.session.remove()
         db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_addlocation_get(self):
        response = self.client.get(url_for('addlocation'))
        self.assertEqual(response.status_code, 405)

    def test_addbird_get(self):
        response = self.client.get(url_for('addbird'))
        self.assertEqual(response.status_code, 405)

    def test_addsighting_get(self):
        response = self.client.get(url_for('addsighting'))
        self.assertEqual(response.status_code, 405)

    def test_updatelocation_get(self):
        response = self.client.get(url_for('updatelocation'))
        self.assertEqual(response.status_code, 405)

    def test_updatebird_get(self):
        response = self.client.get(url_for('updatebird'))
        self.assertEqual(response.status_code, 405)

    def test_updatesighting_get(self):
        response = self.client.get(url_for('updatesighting'))
        self.assertEqual(response.status_code, 405)

    def test_deletelocation_get(self):
        response = self.client.get(url_for('deletelocation'))
        self.assertEqual(response.status_code, 405)

    def test_deletebird_get(self):
        response = self.client.get(url_for('deletebird'))
        self.assertEqual(response.status_code, 405)

    def test_deletesighting_get(self):
        response = self.client.get(url_for('deletesighting'))
        self.assertEqual(response.status_code, 405)



