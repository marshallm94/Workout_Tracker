import os
import pickle
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JesusChristItsJasonBourne'

src_directory = os.path.join(os.getcwd(), "src/")
user_directory = os.path.join(os.getcwd(), "users/")
template_directory = os.path.join(os.getcwd(), "templates/")

with open(os.path.join(user_directory, 'marshall.pickle'), 'rb') as tmp:
	marshall = pickle.load(tmp)

class NameForm(FlaskForm):

	name = StringField('Choose one of the options below: ', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():

	#choices = ['Start Workout', 'Create Split']
	template = os.path.join(template_directory, "options.html")
	return render_template("options.html", user=marshall)


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

