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

	if 'create_workout' in request.form:
		print('creating workout')
	elif 'start_workout' in request.form:
		print('starting workout')
	elif 'check_progress' in request.form:
		print('checking progress')

	return render_template('index2.html', form=form)


@app.route('/user/<name>')
def user(name):

	return render_template('user.html', name=name)

if __name__ == "__main__":

	app.run(debug=True)

