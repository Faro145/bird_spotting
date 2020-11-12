from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Locations

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
