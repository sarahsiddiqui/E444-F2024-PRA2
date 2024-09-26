from . import hello

@hello.route('/hello')
def hello_world():
    return 'Hello, World!'