#!/usr/bin/python3
"""This module creates a local server with flask with 2 routes"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State, City
from os import getenv


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_list():
    """This method uses storage to display the list of cities by states"""

    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    sorted = {
        'states': states
    }
    return render_template('8-cities_by_states.html', **sorted)


@app.teardown_appcontext
def close_storage():
    """This method closes storage session if storage db"""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
