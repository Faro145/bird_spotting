from flask_wtf import FlaskForm
from wtforms import IntegerField, DateTimeField, StringField, SubmitField
from app.models import Birds

class birdForm(FlaskForm):
  scientific_name = StringField('Scientific Name')
  common_name = StringField('Common Name')