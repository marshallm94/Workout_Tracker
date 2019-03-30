from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

	return "<h1>jesus christ it's Jason Bourne...</h1>"

@app.route('/user/<name>')
def user(name):

	return '<h2>Hello {}</h2>'.format(name)

if __name__ == "__main__":

	app.run(debug=True)
