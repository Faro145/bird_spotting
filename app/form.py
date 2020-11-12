from flask_wtf import FlaskForm
from wtforms import IntegerField, DateTimeField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Locations, Birds, Sightings

class CountryCheck:
    def __init__(self, ukcountry, message=none):
        self.ukcountry = ukcountry
        if not message:
            message = "Not a UK country"
        self.message = message

    def __call__(self, locationForm, country):
        if location.country.data.lower() in (word.lower() for word in self.ukcountry):
            raise ValidationError(self.message)

class locationForm(FlaskForm):
  place_name = StringField('Place Name', validators = [DataRequired(),])
  county = StringField('County', validators = [DataRequired(),])
  country = StringField('Country', validators = [DataRequired(), CountryCheck(message="Not a UK Country", ukcountry['Scotland', 'England', 'Northern Ireland', 'Wales']), ])
  submit = SubmitField('Add Location')

class birdForm(FlaskForm):
  scientific_name = StringField('Scientific Name', validators = [DataRequired(),])
  common_name = StringField('Common Name', validators = [DataRequired(),])
  submit = SubmitField('Add Bird')

class sightingForm(FlaskForm):
  location_id = IntegerField('Location ID', validators = [DataRequired(),])
  bird_id = IntegerField('Bird ID', validators = [DataRequired(),])
  recorded = DateTimeField('Recorded', validators = [DataRequired(),])
  gender = StringField('Gender', validators = [DataRequired(),])
  life_stage = StringField('Life Stage', validators = [DataRequired(),])
  number = IntegerField('Number', validators = [DataRequired(),])
  submit = SubmitField('Record Sighting')
