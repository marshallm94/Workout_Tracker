# Overarching goal: Create a single "Workout" object that has:
#
#       - Target sets, reps & % range...
#       - Empty fields (to be filled out during workout) for weight, reps & RPE
#
# for every exercise in todays workout.

# NOTE (2020-09-22): At some point in the flow of information throughout the
# application, the database will need to be referenced. Should this happen here
# (in this file), or in a separate file?

import os
import json

with open(os.path.join('../','data/', 'mesocycle_framework2.json')) as f:
    split = json.load(f)


micro_within_macro = 0
day_within_split = 1

todays_workout = []

# back end
for exercise_dict in split[day_within_split]:
    for exercise, exercise_model in exercise_dict.items():
        exercise_info = {
                exercise: {'Sets': exercise_model['Sets'][micro_within_macro],
                           'Reps': exercise_model['Reps'][micro_within_macro],
                           'RPE': exercise_model['RPE'][micro_within_macro],
                           '% Range': exercise_model['% Range'][micro_within_macro]}}
        todays_workout.append(exercise_info)


# object type: array of dicts - array allows the preservation of exercise order,
# inner dicts allow easily identifiable fields
# presentation
for exercise_dict in todays_workout:
    for exercise, exercise_model in exercise_dict.items():
        # presentation
        print(f"{exercise}")
        for i in range(exercise_model['Sets']):
            out = f"{ exercise_model['Reps'] } @ { exercise_model['RPE'] } in { exercise_model['% Range'] }"
            print(f"\t{out}")



from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, FormField
from wtforms.validators import DataRequired
from flask_table import Table, Col

class WeightForm(FlaskForm):
    weight = FloatField('Weight', [DataRequired()])


class RepForm(FlaskForm):
    reps = IntegerField('Actual Reps', [DataRequired()])


class RPEForm(FlaskForm):
    rpe = FloatField('Actual RPE')


class Set(object):
    def __init__(self, target_reps, target_rpe, target_percentage_range):
        self.target_reps = target_reps
        self.target_rpe = target_rpe
        self.target_percentage_range = target_percentage_range
        self.weight = WeightForm()
        self.reps = RepForm()
        self.rpe = RPEForm()


class ExerciseSet(Table):
    # NOTE: the order that the attributes are listed here (top to bottom) is
    # the order the will be displayed in the table (left to right).
    target_reps = Col("Target Reps")
    target_rpe = Col("Target RPE")
    target_percentage_range = Col('Target % Range') 

    weight = Col("Weight")
    reps = Col('Reps')
    rpe = Col('RPE')


sets = [Set(target_reps = 6, target_rpe = 7),
        Set(target_reps = 6, target_rpe = 7),
        Set(target_reps = 6, target_rpe = 7),
        Set(target_reps = 6, target_rpe = 7)]

# class WorkoutTable(object):
#     def __init__(self):
#         self.mesocycle_related_notes = None
#         self.workout_related_notes = None
#         self.workout = 'list of ExerciseSet objects'







