from flask_wtf import FlaskForm

from wtforms import FieldList, StringField
from wtforms.validators import DataRequired

from flask_table import Table, Col


class WorkoutTable(FlaskForm):

    label = 'Exercise'
    exercises = FieldList(StringField('Exercise'), min_entries = 1)

    def add_exercise(self):

        exercises.append(StringField('Exercise'))
