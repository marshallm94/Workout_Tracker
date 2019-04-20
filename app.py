import os
import pickle
from flask import Flask, render_template, url_for
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
	
	return render_template("index2.html", form=form)

	


#@app.route('/tmp', methods=['GET','POST'])
#def tmp():
#
#	name = None
#	form = NameForm()
#
#	if form.validate_on_submit():
#		name = form.name.data
#		form.name.data = '' 
#	print(form.name.data)
#	return render_template('index.html', form=form, name=name)


@app.route('/user/<name>')
def user(name):

	return render_template('user.html', name=name)

if __name__ == "__main__":

	app.run(debug=True)

