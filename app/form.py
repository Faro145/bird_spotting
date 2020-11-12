from flask_wtf import FlaskForm
from wtforms import IntegerField, DateTimeField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Locations, Birds, Sightings

class locationForm(FlaskForm):
  place_name = StringField('Place Name', validators = [DataRequired(),])
  county = StringField('County', validators = [DataRequired(),])
  country = StringField('Country', validators = [DataRequired(),])
  submit = SubmitField('Add Location')

  def validate_country(self, country):
      ukcountry = [Scotland, England, Northern Ireland, Wales]
      for location in locations:
          if location.country != ukcountry:
              raise ValidationError('Not a country in the UK')

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
