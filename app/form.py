from flask_wtf import FlaskForm
from wtforms import IntegerField, DateTimeField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Locations, Birds, Sightings

class CountryCheck:
    def __init__(self, ukcountry, message):
        self.ukcountry = ukcountry
        if not message:
            message = "Not a UK country"
        self.message = message

    def __call__(self, form, field):
        if field.data != self.ukcountry[0] and field.data != self.ukcountry[1] and field != self.ukcountry[2] and field != self.ukcountry[3]:
            raise ValidationError(self.message)

class locationForm(FlaskForm):
  place_name = StringField('Place Name', validators = [DataRequired(),])
  county = StringField('County', validators = [DataRequired(),])
  country = StringField('Country', validators = [DataRequired(), CountryCheck(ukcountry = ['Scotland', 'England', 'Northern Ireland', 'Wales'], message="Not a UK Country"), ])
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
