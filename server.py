import os
from src import WorkoutTable
import pickle

from flask import Flask, render_template, url_for, request, redirect
from flask_table import Table, Col

from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JesusChristItsJasonBourne'

src_directory = os.path.join(os.getcwd(), "src/")
user_directory = os.path.join(os.getcwd(), "users/")

with open(os.path.join(user_directory, 'marshall.pickle'), 'rb') as tmp:
    marshall = pickle.load(tmp)


@app.route('/', methods=['GET','POST'])
def index():

    return render_template('index.html')

@app.route('/continue_macrocycle')
def continue_macrocycle():

    return render_template('continue_macrocycle.html')

@app.route('/create_macrocycle', methods=['GET','POST'])
def create_macrocycle():

    if request.method == 'GET':

        return render_template('create_macrocycle.html')

    elif request.method == 'POST':

        split_length = int(request.form['split_length'])
        # TODO: create workout template here and then pass
        # entire object to render_template()

        split = [WorkoutTable() for _ in range(split_length)]

        return render_template('create_microcycle.html', split=split)

@app.route('/create_microcycle', methods=['GET','POST'])
def create_microcycle():

    if request.method == 'GET':
        print("get")
        pass

    elif request.method == 'POST':
        print('bingbong')
        print(request.form)
        #if request.form['add_exercise']:
        pass

    return render_template('create_microcycle.html')

@app.route('/create_periodization_models', methods=['GET','POST'])
def create_periodization_models():

    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        #if request.form['add_exercise']:
        pass

    return render_template('create_periodization_models.html')

@app.route('/start_one_off_workout', methods=['GET','POST'])
def workout_home():

    header = 'Choose one of the workouts below:'
    title = 'Start Workout'

    splits = marshall.splits

    return render_template('workout_home.html', header=header, title=title, splits=splits)


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

