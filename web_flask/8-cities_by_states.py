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
    for key, val in states.items():
        sort = sorted(val.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=val, cities=sort)


@app.teardown_appcontext
def close_storage():
    """This method closes storage session if storage db"""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
