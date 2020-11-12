from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app.models import Birds

class birdForm(FlaskForm):
  scientific_name = StringField('Scientific Name', validators = [DataRequired(),])
  common_name = StringField('Common Name', validators = [DataRequired(),])
  submit = SubmitField('Add Bird')
