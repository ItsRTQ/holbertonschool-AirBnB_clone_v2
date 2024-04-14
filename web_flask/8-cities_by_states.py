#!/usr/bin/python3
"""This module creates a local server with flask with 2 routes"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State, City
from os import getenv


app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def cities_by_states():
    """This method uses storage to display the list of cities by states"""

    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def close_storage():
    """This method closes storage session if storage db"""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
