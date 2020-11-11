from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from app.models import Locations

class locationForm(FlaskForm):
  place_name = StringField('Place Name')
  county = StringField('County')
  country = StringField('Country')
  submit = SubmitField('Add Location')
