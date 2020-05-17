from Workout_Tracker import app

from flask import request, render_template, url_for, redirect

import os
import json

data_directory = os.path.join("Workout_Tracker", "data/")
examples_directory = os.path.join("Workout_Tracker", "examples/")

with open(os.path.join(data_directory, 'display_mesocycle.json')) as f:
    display_meso = json.load(f)
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

    #return render_template('index.html',tmp=exercise_table)
    return render_template('index.html')

@app.route('/review_mesocycle', methods=['GET','POST'])
def review_mesocycle():

    meso_length = 3
    return render_template('review_mesocycle.html',
            split = display_meso,
            meso_length = meso_length)

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
