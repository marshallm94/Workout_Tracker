from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import os
import jinja2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JesusChristItsJasonBourne'

class NameForm(FlaskForm):

	name = StringField('What is your name? ', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():

	name = None
	form = NameForm()

	if form.validate_on_submit():
		name = form.name.data
		form.name.data = '' 
	print(form.name.data)
	return render_template('index.html', form=form, name=name)


@app.route('/user/<name>')
def user(name):

	return render_template('user.html', name=name)

if __name__ == "__main__":

	app.run(debug=True)
