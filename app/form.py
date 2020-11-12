from flask_wtf import FlaskForm
from wtforms import IntegerField, DateTimeField, StringField, SubmitField
from wtforms.validators import DataRequired
from app.models import Sightings

class sightingForm(FlaskForm):
  location_id = IntegerField('Location ID', validators = [DataRequired(),])
  bird_id = IntegerField('Bird ID', validators = [DataRequired(),])
  recorded = DateTimeField('Recorded', validators = [DataRequired(),])
  gender = StringField('Gender', validators = [DataRequired(),])
  life_stage = StringField('Life Stage', validators = [DataRequired(),])
  number = IntegerField('Number', validators = [DataRequired(),])
  submit = SubmitField('Record Sighting')
