from flask_wtf import FlaskForm, Form

from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

from flask_table import Table, Col


class WorkoutTable(Form):

    def __init__(self):

        exercise = Col('Exercise')

    def add_exercise(self, name):

        self.items.append(Exercise(name))


class Exercise(object):

    def __init__(self, name):

        self.name = name


#class WorkoutTable(Table):
#
#    exercise = Col('Exercise')

