#!/usr/bin/python3
"""
starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """fetching data from the storage engine"""
    state = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', state=state, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
