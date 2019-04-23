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

class OptionForm(FlaskForm):

	heading = 'Choose one of the options below:'
	start_workout = SubmitField('Start Workout')
	create_workout = SubmitField('Create Workout')
	check_progress = SubmitField('Check Progress')
	

@app.route('/', methods=['GET','POST'])
def index():

	form = OptionForm()
	
	if request.method == 'POST':

		if 'create_workout' in request.form:

			print('creating workout')

		elif 'start_workout' in request.form:

			print('starting workout')

		elif 'check_progress' in request.form:

			print('checking progress')
	
	elif request.method == 'GET':

		pass

	return render_template('index.html', form=form)


@app.route('/start_workout')
def start_workout():

	return render_template('start_workout.html')


@app.route('/create_workout')
def create_workout():

	return render_template('create_workout.html')


@app.route('/check_progress')
def check_progress():

	return render_template('check_progress.html')


if __name__ == "__main__":

	app.run(debug=True)

