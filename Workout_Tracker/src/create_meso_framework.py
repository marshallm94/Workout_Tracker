from app import app

from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, FormField
from wtforms.validators import DataRequired
from flask_table import Table, Col

class WeightForm(FlaskForm):

    weight = FloatField('Weight', [DataRequired()])

class RepForm(FlaskForm):

    reps = IntegerField('Actual Reps', [DataRequired()])

class RPEForm(FlaskForm):

    rpe = FloatField('Actual RPE', [DataRequired()])

class Set(object):

    def __init__(self, target_reps, target_rpe):

        self.target_reps = target_reps
        self.target_rpe = target_rpe
        self.weight = WeightForm()
        self.reps = RepForm()
        self.rpe = RPEForm()

class ExerciseTable(Table):
    # NOTE: the order that the attributes are listed here (top to bottome) is
    # the order the will be displayed in the table (left to right).
    target_reps = Col("Target Reps")
    target_rpe = Col("Target RPE")
    weight = Col("Weight")
    reps = Col('Reps')
    rpe = Col('RPE')

sets = [Set(target_reps = 6, target_rpe = 7),
        Set(target_reps = 6, target_rpe = 7),
        Set(target_reps = 6, target_rpe = 7),
        Set(target_reps = 6, target_rpe = 7)]

exercise_table = ExerciseTable(sets)

# for day in split:
#     for exercise_dict in day:
#         for exercise_name, progression_dict in exercise_dict.items():


