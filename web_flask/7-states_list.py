#!/usr/bin/python3
"""
starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """use storage for fetching data from the storage engine """
    states = sorted(list(storage.all("State").values()), key=lambda h: h.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
