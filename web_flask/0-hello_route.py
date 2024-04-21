#!/usr/bin/python3
"""script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


# run the application
if __name__ == "__main__":
    """run the app"""
    app.run(host='0.0.0.0', port=5000)
