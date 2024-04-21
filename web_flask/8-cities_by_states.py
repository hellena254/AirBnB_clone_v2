#!/usr/bin/python3
"""
starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ fetching data from the storage engine"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
