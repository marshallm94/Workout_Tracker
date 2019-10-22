import os
import pickle
from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
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


@app.route('/workout_home', methods=['GET','POST'])
def workout_home():

	header = 'Choose one of the workouts below:'
	title = 'Start Workout'

	splits = marshall.splits

	return render_template('workout_home.html', header=header, title=title, splits=splits)


@app.route('/create_workout')
def create_workout():

	return render_template('create_workout.html')


@app.route('/check_progress')
def check_progress():

	return render_template('check_progress.html')


@app.route('/start_workout', methods=['GET','POST'])
def start_workout():


	return render_template('start_workout.html')


if __name__ == "__main__":

	app.run(debug=True)

