#!/usr/bin/python3
"""This module will start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


def sort_data(to_sort):
    """sorts the data loaded from storage"""

    return sorted(to_sort, key=lambda x: x.name)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the current SQLAlchemy session."""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filters_html():
    """Display a Flask web application based on storage fetched data."""
    states = storage.all(State)
    amenities = storage.all(Amenity)

    sorted_states = sort_data(states.values())
    sorted_amenities = sort_data(amenities.values())

    return render_template(
        "10-hbnb_filters.html",
        states=sorted_states,
        amenities=sorted_amenities
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
