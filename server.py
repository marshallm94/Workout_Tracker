import os
from src import WorkoutTable
import json

from flask import Flask, request, session
from flask import render_template, url_for, redirect
from flask_table import Table, Col

from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JesusChristItsJasonBourne'

src_directory = os.path.join(os.getcwd(), "src/")
user_directory = os.path.join(os.getcwd(), "users/")
data_directory = os.path.join(os.getcwd(), "data/")
examples_directory = os.path.join(os.getcwd(), "examples/")

with open(os.path.join(data_directory, 'planned_mesocycle.json')) as f:
    planned_meso = json.load(f)
with open(os.path.join(data_directory, 'stage1.json')) as f:
    stage_1 = json.load(f)
with open(os.path.join(data_directory, 'stage2.json')) as f:
    stage_2 = json.load(f)
with open(os.path.join(data_directory, 'stage3.json')) as f:
    stage_3 = json.load(f)

with open(os.path.join(examples_directory, 'progression_model.json')) as f:
    progression_example = json.load(f)

@app.route('/', methods=['GET','POST'])
def index():

    return render_template('index.html')

@app.route('/review_mesocycle', methods=['GET','POST'])
def review_mesocycle():

    return render_template('review_mesocycle.html', mesocycle=planned_meso)

@app.route('/continue_mesocycle')
def continue_mesocycle():

    return render_template('continue_mesocycle.html')

@app.route('/create_mesocycle', methods=['GET','POST'])
def create_mesocycle():

    if request.method == 'GET':

        return render_template('create_mesocycle.html')

    elif request.method == 'POST':

        # split_length = int(request.form['split_length'])
        # # TODO: create workout template here and then pass
        # # entire object to render_template()

        # split = [WorkoutTable() for _ in range(split_length)]

        return render_template('create_microcycle.html', split=stage_2)

@app.route('/create_microcycle', methods=['GET','POST'])
def create_microcycle():

    if request.method == 'GET':
        print("get")
        pass

    elif request.method == 'POST':

        pass

    return render_template('create_microcycle.html')

@app.route('/create_periodization_models', methods=['GET','POST'])
def create_periodization_models():

    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        # TODO: add periodation models to session object?
        pass

    return render_template('create_periodization_models.html',
            models = stage_3,
            example = progression_example)

@app.route('/create_one_off_workout')
def create_workout():

    return render_template('create_workout.html')


@app.route('/check_progress')
def check_progress():

    return render_template('check_progress.html')


@app.route('/start_one_off_workout', methods=['GET','POST'])
def start_workout():


    return render_template('start_workout.html')


if __name__ == "__main__":
    app.run(debug=True)

