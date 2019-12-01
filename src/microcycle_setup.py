from flask_wtf import FlaskForm

from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

from flask_table import Table, Col


class WorkoutTable(FlaskForm):

    exercise = StringField('Exercise')


class Exercise(object):

    def __init__(self):

        self.name

