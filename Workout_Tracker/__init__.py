from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JesusChristItsJasonBourne'

from Workout_Tracker.views import *

if __name__ == "__main__":
    app.run(debug=True)

