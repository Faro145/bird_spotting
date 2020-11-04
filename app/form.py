from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateTimeField, StringField, SubmitField
from app.models import Todo

class sightingForm(Flaskform):
  id = IntegerField('ID')
  location_id = IntegerField('Location ID')
  bird_id = IntegerField('Bird ID')
  recorded = DateTimeField('Recorded')
  gender = StringField('Gender')
  life_stage = StringField('Life Stage')
  number = IntegerField('Number')
  submit = SubmitField('Record Sighting')
