from flask import Flask

# from . import hello

app = Flask(__name__)
@app.route('/')
def index():
    print("Something ran")
    return '<h1>Hello World!</h1>'