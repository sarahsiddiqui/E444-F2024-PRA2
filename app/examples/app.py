from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    print("Something ran")
    return '<h1>Hello World!</h1>'