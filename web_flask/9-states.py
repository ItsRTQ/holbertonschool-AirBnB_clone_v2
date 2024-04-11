#!/usr/bin/python3
"""This module creates a flask eviroment to display html pages"""
from flask import Flask, render_template
from models import storage
from models.state import State, City
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """This method will close the SQLAlchemy session on teardown"""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        storage.close()


@app.route('/states', defaults={"id": None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """This method displays a states list or state in detail"""

    if id is None:
        states = storage.all(State)
        sorted_states = sorted(states.values(), key=lambda state: state.name)
        
        return render_template('9-states.html', states=sorted_states)
    else:
        states = storage.all(State)
        for key, value in states.items():
            if str(id) in key:
                sorted_cities = sorted(value.cities, key=lambda city: city.name)
                return render_template('9-states.html', state=value, cities=sorted_cities)
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
