from flask_wtf import FlaskForm, Form

from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

from flask_table import Table, Col


class WorkoutTable(Form):

    exercise = StringField('Exercise')


class Exercise(object):

    def __init__(self):

        self.name

