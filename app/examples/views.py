from flask import Flask, render_template

from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    currentDate = datetime.now()
    timeString = currentDate.strftime("The local date and time is %A, %B %d, %Y %I:%M %p")
    return render_template('user.html', name=name, current_time=timeString)