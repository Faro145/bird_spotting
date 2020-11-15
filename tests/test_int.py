import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app import app, db
from app.models import Locations, Birds, Sightings

test_bird_scientific_name = "Turdus merula"
test_bird_common_name = "Blackbird"
test_location_place_name = "Bennachie"
test_location_county = "Aberdeenshire"
test_location_country = "Scotland"
test_sighting_location_id = 1
test_sighting_bird_id = 1
test_sighting_recorded = "13/02/17"
test_sighting_gender = "Female"
test_sighting_life_stage = "Adult"
test_sighting_number = 4

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URI')
        app.config['SECRET_KEY'] = getenv('KEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="<PATH TO chromedriver executable>", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)
 
class TestSighting(TestBase):

    def test_location(self):
        self.driver.find_element_by_xpath("<xpath for Add Location button in nav bar>").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('<xpath for location place name>').send_keys(test_location_place_name)
        self.driver.find_element_by_xpath('<xpath for location county>').send_keys(test_location_county)
        self.driver.find_element_by_xpath('<xpath for location country>').send.keys(test_location_country)
        self.driver.find_element_by_xpath('<xpath for submit button>').click()
        time.sleep(1)
        
        assert url_for('index') in self.driver.current_url

    def test_bird(self):
        self.driver.find_element_by_xpath("<xpath for Add Bird button in nav bar>").click()
        time.sleep(1)
    
        self.driver.find_element_by_xpath('<xpath for bird scientific name>').send_keys(test_bird_scientific_name)
        self.driver.find_element_by_xpath('<xpath for bird common name>').send_keys(test_bird_common_name)
        self.driver.find_element_by_xpath('<xpath for submit button>').click()
        time.sleep(1)
    
        assert url_for('index') in self.driver.current_url
    
    def test_sighting(self):
        self.driver.find_element_by_xpath("<xpath for Register button in nav bar>").click()
        time.sleep(1)
        
        self.driver.find_element_by_xpath('<xpath for sighting location id>').send_keys(test_sighting_location_id)
        self.driver.find_element_by_xpath('<xpath for sighting bird id>').send_keys(test_sighting_bird_id)
        self.driver.find_element_by_xpath('<xpath for sighting recorded>').send_keys(test_sighting_recorded)
        self.driver.find_element_by_xpath('<xpath for sighting gender>').send_keys(test_sighting_gender)
        self.driver.find_element_by_xpath('<xpath for sighting life stage>').send_keys(test_sighting_life_stage)
        self.driver.find_element_by_xpath('<xpath for sighting number>').send_keys(test_sighting_number)
        self.driver.find_element_by_xpath('<xpath for register button>').click()
        time.sleep(1)
        
        assert url_for('index') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)
