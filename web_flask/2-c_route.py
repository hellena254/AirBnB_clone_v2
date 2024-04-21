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
def c_is_fun():
    """display “C ” followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    """run the application"""
    app.run(host='0.0.0.0', port=5000)
