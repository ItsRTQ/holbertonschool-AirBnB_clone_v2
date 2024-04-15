#!/usr/bin/python3
"""This module will start a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State, City
from models.amenity import Amenity
from os import getenv

app = Flask(__name__)


def key_spliter(to_split):
    parts = to_split.split('.')
    if len(parts) > 1:
        return parts[1]
    else:
        return to_split

def sort_data(to_sort={}):
    sorting = {}
    for key, value in to_sort.items():
        sorting[key_spliter(key)] = value
    sorted_keys = sorted(sorting.keys())
    sorted_dict = {key: sorting[key] for key in sorted_keys}
    return sorted_dict


@app.teardown_appcontext
def teardown_db(exception):
    """This method will close the SQLAlchemy session on teardown"""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filters_html():
    """Display flask web application, based on storage fetch data"""

    states = storage.all(State)
    amenities = storage.all(Amenity)
    sort = sort_data(states)
    sorting = {}
    ame_sort = []
    for key, val in sort.items():
        sorting[key] = sorted(val.cities, key=lambda city: city.name)
    for value in amenities.values():
        ame_sort.append(value.name)
    ame_srtd = sorted(ame_sort)
    return render_template("10-hbnb_filters.html", state=sorting, ame=ame_srtd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
