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


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """display only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Route to display a HTML page with "Number: n" if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """display a HTML page with "Number: n is even|odd" if n is an integer"""
    odd_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)


if __name__ == "__main__":
    """run the application"""
    app.run(host='0.0.0.0', port=5000)
