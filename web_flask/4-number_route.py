#!/usr/bin/python3
"""script that starts a Flask web application
/: display “Hello HBNB!”
/hbnb: display “HBNB”"""

from flask import Flask
# create a flask application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ display Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """display “C ” followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """display “Python ”, followed by the value of the text"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>' strict_slashes=False)
def display_number(n):
    """display only if n is an integer"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    """run the application"""
    app.run(host='0.0.0.0', port=5000)
